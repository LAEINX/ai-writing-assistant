"""AI 写作工具 - 配置文件"""

import os
from pathlib import Path


class Config:
    """项目配置类"""
    
    # 项目根目录
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # API 密钥（从环境变量读取）
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN", "")
    
    # LLM 模型配置
    DEFAULT_MODEL = "gpt-4o"
    MAX_TOKENS = 4096
    TEMPERATURE = 0.7
    
    # 输出目录
    OUTPUT_DIR = BASE_DIR / "output"
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # 日志配置
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
