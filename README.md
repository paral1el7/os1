# CyberWise - 智能知识管理系统

[![Netlify Status](https://api.netlify.com/api/v1/badges/94462979-6af1-428e-a71f-e6af617632a1/deploy-status)](https://app.netlify.com/sites/cyberwise/deploys)

## 🌟 项目简介

CyberWise 是一个现代化的个人知识管理系统，集成了用户认证、笔记管理、AI 写作助手和知识库搜索功能。采用纯前端架构，支持离线使用，数据安全可靠。

## 🚀 在线体验

**官方网站**: [https://cyberwise.netlify.app](https://cyberwise.netlify.app)

## ✨ 主要功能

### 🔐 用户认证系统

- Firebase Authentication 集成
- 邮箱注册/登录
- 密码可见性切换
- 安全的用户会话管理

### 📝 笔记管理

- 创建、编辑、删除笔记
- 本地存储，支持离线使用
- 笔记收藏功能
- 内容预览和搜索

### 🤖 AI 写作助手

- 智能内容生成
- 多种模板（文章、总结、教程）
- 自动标题生成
- AI 内容直接保存为笔记

### 📚 知识库搜索

- 385 个技术问题数据库
- 关键词搜索和分类筛选
- 人工答案与 AI 答案对比
- 响应式搜索界面

### 🌍 多语言支持

- 中英文切换
- 本地化存储设置
- 完整界面翻译

### 🎨 现代化界面

- 响应式设计
- 暗色主题
- 渐变色彩方案
- 平滑动画效果

## 🛠️ 技术栈

### 前端

- **HTML5** - 语义化结构
- **CSS3** - 现代样式和动画
- **JavaScript (ES6+)** - 核心功能逻辑
- **RemixIcon** - 图标系统

### 后端服务

- **Firebase Authentication** - 用户认证
- **Firebase Firestore** - 云端数据存储（可选）
- **LocalStorage** - 本地数据存储

### 部署

- **Netlify** - 静态网站托管
- **GitHub** - 源代码管理

## 📁 项目结构

```
cyberwise_new/
├── templates/                 # HTML页面
│   ├── login.html            # 登录页面
│   ├── register.html         # 注册页面
│   ├── dashboard.html        # 主仪表板
│   └── knowledge_base.html   # 知识库页面
├── static/
│   ├── css/
│   │   └── style.css         # 统一样式文件
│   ├── js/
│   │   ├── firebase-init.js  # Firebase配置
│   │   ├── login.js          # 登录逻辑
│   │   ├── register.js       # 注册逻辑
│   │   ├── dashboard.js      # 仪表板功能
│   │   └── language.js       # 多语言支持
│   └── data/
│       ├── questions_dataset.json  # 问题数据集
│       └── dataset_stats.json      # 数据统计
├── netlify.toml              # Netlify配置
└── README.md                 # 项目文档
```

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/YungSongWang/Cyberwise.git
cd Cyberwise
```

### 2. 本地运行

```bash
# 使用Python启动本地服务器
python -m http.server 8000

# 或使用Node.js
npx serve .
```

### 3. 访问应用

打开浏览器访问：`http://localhost:8000/templates/login.html`

## ⚙️ 配置说明

### Firebase 配置

项目使用 Firebase 作为认证和数据存储后端。如需自定义配置，请修改 `static/js/firebase-init.js` 文件中的配置信息。

### 环境变量

项目支持以下配置选项：

- **语言设置**: 自动保存在 localStorage
- **主题设置**: 默认暗色主题
- **存储模式**: 本地存储优先

## 📱 功能特性

### 🔒 离线优先

- 所有笔记本地存储
- 无网络环境下正常使用
- 网络恢复时自动同步

### 🎯 用户体验

- 统一的模态框设计
- 键盘快捷键支持
- 响应式移动端适配

### 📊 数据管理

- 笔记导入/导出（规划中）
- 数据备份与恢复
- 跨设备同步（规划中）

## 🔄 版本历史

### v2.1.0 (2025-05-29)

- ✨ 增强 AI Writing 功能
- 🎨 统一模态框界面设计
- 🐛 修复用户信息显示不一致
- ⚡ 强制缓存刷新机制

### v2.0.0 (2025-05-28)

- 🎉 完整知识库搜索功能
- 📝 纯本地存储笔记系统
- 🌍 多语言支持
- 🎨 现代化 UI 设计

### v1.0.0 (2025-05-27)

- 🔐 基础用户认证
- 📝 笔记创建和管理
- 🚀 项目初始版本

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📞 联系方式

- **作者**: YungSongWang
- **邮箱**: yunsong2023uk@163.com
- **GitHub**: [@YungSongWang](https://github.com/YungSongWang)
- **项目地址**: [https://github.com/YungSongWang/Cyberwise](https://github.com/YungSongWang/Cyberwise)

## 🙏 致谢

感谢以下开源项目的支持：

- [Firebase](https://firebase.google.com/) - 后端服务
- [RemixIcon](https://remixicon.com/) - 图标库
- [Netlify](https://www.netlify.com/) - 部署平台

---

⭐ 如果这个项目对你有帮助，请给它一个星标！

# 触发新部署
