import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 设置matplotlib支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def load_custom_dictionary(dictionary_path='new_dic_vader_for_IT.dic'):
    """
    Load custom sentiment dictionary from the IT-specific dictionary file
    Format: word    score    std_dev    [scores]
    Example: $:    -1.5    0.80623    [-1, -1, -1, -1, -3, -1, -3, -1, -2, -1]
    """
    custom_dict = {}
    try:
        with open(dictionary_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):  # Skip empty lines and comments
                    continue
                try:
                    # First split by tab
                    parts = line.split('\t')
                    if len(parts) >= 2:
                        # Get the word (which might contain spaces)
                        word = parts[0].strip()
                        # Get the score from the second part
                        score = float(parts[1].strip())
                        custom_dict[word] = score
                    else:
                        # If no tab, try splitting by multiple spaces
                        parts = line.split()
                        if len(parts) >= 2:
                            # Try to find where the score starts
                            for i in range(len(parts)):
                                try:
                                    score = float(parts[i])
                                    # Everything before this is the word
                                    word = ' '.join(parts[:i])
                                    custom_dict[word] = score
                                    break
                                except ValueError:
                                    continue
                        else:
                            print(f"Warning: Line {line_num} has invalid format: {line}")
                except ValueError as e:
                    print(f"Warning: Could not parse line {line_num}: {line}")
                    print(f"Error details: {e}")
                    continue
        print(f"Successfully loaded {len(custom_dict)} words from dictionary")
        return custom_dict
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        return None

def analyze_sentiment(text, use_custom_dict=True):
    analyzer = SentimentIntensityAnalyzer()
    
    # Load and update with custom dictionary
    if use_custom_dict:
        custom_dict = load_custom_dictionary()
        if custom_dict:
            analyzer.lexicon.update(custom_dict)
    
    sentiment_scores = analyzer.polarity_scores(text)
    compound = sentiment_scores['compound']
    
    if compound > 0.05:
        sentiment = 'positive'
    elif compound < -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
        
    return compound, sentiment

def find_top_similar_texts(input_text, excel_path, top_n=5):
    """
    Calculate similarity between input text and all texts in Excel, output top_n most similar ones
    """
    # Load model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    # Read Excel
    df = pd.read_excel(excel_path)
    # Assume text is in first column
    texts = df.iloc[:, 0].astype(str).tolist()
    # Encode
    input_emb = model.encode(input_text)
    texts_emb = model.encode(texts)
    # Calculate similarity
    sims = cosine_similarity([input_emb], texts_emb)[0]
    # Get indices of top_n highest similarity
    top_indices = sims.argsort()[-top_n:][::-1]
    # Output results
    print(f"\nTop {top_n} most similar texts:")
    for idx in top_indices:
        print(f"Text: {texts[idx]}\nSimilarity: {sims[idx]:.4f}\n")

def test_classifier(text, use_custom_dict=True):
    # Sentiment analysis
    compound, sentiment = analyze_sentiment(text, use_custom_dict)
    print(f"\nSentiment Analysis Results:")
    print(f"Compound Score: {compound:.3f}")
    print(f"Sentiment: {sentiment}")
    
    # Load model and scaler
    svm = joblib.load('svm_classifier.joblib')
    scaler = joblib.load('scaler.joblib')
    keyword_to_index = joblib.load('keyword_to_index.joblib')
    
    # Create feature vector
    features = np.zeros(len(keyword_to_index))
    for keyword in text.lower().split():
        if keyword in keyword_to_index:
            features[keyword_to_index[keyword]] = 1
    
    # Scale features
    features_scaled = scaler.transform(features.reshape(1, -1))
    
    # Predict
    prediction = svm.predict(features_scaled)
    probabilities = svm.predict_proba(features_scaled)
    
    # Get probabilities for all classes
    classes = svm.classes_
    class_probs = [(classes[i], prob) for i, prob in enumerate(probabilities[0])]
    class_probs.sort(key=lambda x: x[1], reverse=True)
    
    # Print classification results
    print(f"\nInput Text: {text}")
    print(f"\nPredicted Category: {prediction[0]}")
    print("\nCategory Probabilities:")
    for category, prob in class_probs:
        print(f"{category}: {prob:.2%}")

    # Plot probability distribution pie chart
    threshold = 0.05
    labels = []
    sizes = []
    others_prob = 0.0
    for category, prob in class_probs:
        if prob >= threshold:
            labels.append(category)
            sizes.append(prob)
        else:
            others_prob += prob
    if others_prob > 0:
        labels.append('Others')
        sizes.append(others_prob)
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Category Probability Distribution')
    plt.axis('equal')
    plt.show()

    # Calculate similarity
    find_top_similar_texts(text, 'task 4.xlsx', top_n=5)

# Test cases
test_cases = [
    "The user authentication system needs to be improved for better security",
    "We found a memory leak in the application that needs to be fixed",
    "The SSL certificate needs to be updated for the server",
    "There is a build error in the latest version",
    "We need to add new features to the user interface",
    "The system is experiencing high CPU usage",
    "The password reset functionality is not working properly",
    "We need to update the dependencies to fix compatibility issues"
]

print("Starting classifier test...")
for test_text in test_cases:
    test_classifier(test_text)
    print("\n" + "="*50 + "\n")

# Interactive testing
while True:
    user_input = input("\nEnter text to classify (enter 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    test_classifier(user_input) 