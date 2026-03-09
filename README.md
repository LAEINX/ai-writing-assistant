# 🤖 AI Writing Assistant

一个基于 LLM 的智能写作工具，支持多种文体创作、润色和翻译。

## ✨ 功能特性

- 📝 **智能写作** - 根据提示生成高质量内容
- 🔄 **文本重写** - 支持多种风格的专业改写
- 📋 **内容总结** - 快速提取核心要点
- 🔧 **模块化设计** - 易于扩展和定制

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/LAEINX/ai-writing-assistant.git
cd ai-writing-assistant
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 OpenAI API Key
nano .env
```

### 4. 运行程序

```bash
python src/main.py
```

## 📦 项目结构

```
ai-writing-assistant/
├── src/                    # 源代码目录
│   ├── __init__.py         # 包初始化
│   ├── config.py           # 配置文件
│   ├── main.py             # 主程序入口
│   └── writer/             # 写作模块
│       ├── __init__.py     # writer 包
│       └── core.py         # 核心写作引擎
├── requirements.txt        # Python 依赖
├── .env.example           # 环境变量示例
├── .gitignore             # Git 忽略配置
└── README.md              # 项目说明
```

## 🔑 API Key 获取

1. **OpenAI API**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. **Hugging Face Token**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

## 📝 使用示例

```python
from src.writer import AIWriter

# 创建写作引擎
writer = AIWriter(model="gpt-4o", temperature=0.7)

# 生成内容
result = writer.generate("写一封求职信")
print(result)

# 重写文本
rewritten = writer.rewrite("你好，很高兴认识你。", style="professional")
print(rewritten)

# 总结长文
summary = writer.summarize("很长的文章内容...", max_length=200)
print(summary)
```

## 🛠️ 开发计划

- [ ] 添加更多写作模板（邮件、报告、故事等）
- [ ] 支持本地 LLM 模型（Llama, Qwen 等）
- [ ] Web UI 界面
- [ ] CLI 命令行工具
- [ ] API 服务接口

## 📄 License

MIT License - 自由使用，欢迎贡献！

## 👨‍💻 作者

**LAEINX** - AI 产品经理 & 开发者

---

⭐ **喜欢这个项目？请给个 Star 支持一下！**
