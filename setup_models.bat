@echo off
echo Setting up model files...

:: 检查test目录是否存在
if not exist "test" (
    echo Error: test directory not found!
    echo Please make sure you are running this script from the project root directory.
    pause
    exit /b 1
)

:: 创建必要的目录
if not exist "models" mkdir models
if not exist "data" mkdir data

:: 复制模型文件
echo Copying model files...

:: 复制并重命名Excel文件（处理空格）
if exist "test\task 4.xlsx" (
    copy "test\task 4.xlsx" "data\task_4.xlsx"
    if errorlevel 1 (
        echo Error copying task 4.xlsx
        pause
        exit /b 1
    )
) else (
    echo Error: task 4.xlsx not found in test directory
    pause
    exit /b 1
)

:: 复制其他模型文件
if exist "test\svm_classifier.joblib" (
    copy "test\svm_classifier.joblib" "models\svm_classifier.joblib"
    if errorlevel 1 (
        echo Error copying svm_classifier.joblib
        pause
        exit /b 1
    )
) else (
    echo Error: svm_classifier.joblib not found in test directory
    pause
    exit /b 1
)

if exist "test\scaler.joblib" (
    copy "test\scaler.joblib" "models\scaler.joblib"
    if errorlevel 1 (
        echo Error copying scaler.joblib
        pause
        exit /b 1
    )
) else (
    echo Error: scaler.joblib not found in test directory
    pause
    exit /b 1
)

if exist "test\keyword_to_index.joblib" (
    copy "test\keyword_to_index.joblib" "models\keyword_to_index.joblib"
    if errorlevel 1 (
        echo Error copying keyword_to_index.joblib
        pause
        exit /b 1
    )
) else (
    echo Error: keyword_to_index.joblib not found in test directory
    pause
    exit /b 1
)

if exist "test\new_dic_vader_for_IT.dic" (
    copy "test\new_dic_vader_for_IT.dic" "models\new_dic_vader_for_IT.dic"
    if errorlevel 1 (
        echo Error copying new_dic_vader_for_IT.dic
        pause
        exit /b 1
    )
) else (
    echo Error: new_dic_vader_for_IT.dic not found in test directory
    pause
    exit /b 1
)

echo All files copied successfully!
echo.
echo Verifying files...
dir models
dir data
echo.
echo Setup completed successfully!
pause 