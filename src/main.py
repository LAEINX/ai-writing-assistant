#!/usr/bin/env python3
"""AI 写作工具 - 主程序入口"""

import sys
import os
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console
from rich.panel import Panel
from rich import box

from src.writer import AIWriter


def print_welcome():
    """打印欢迎界面"""
    console = Console()
    
    welcome_text = """
🤖 [bold blue]AI Writing Assistant[/bold blue] v0.1.0
    
[italic]智能写作助手 - 让你的创作更高效！[/italic]
    """
    
    console.print(Panel(welcome_text, box=box.DOUBLE, border_style="blue"))


def main():
    """主函数"""
    print_welcome()
    
    # 检查 API Key
    if not os.getenv("OPENAI_API_KEY"):
        console = Console()
        console.print("[red]❌ 错误：未设置 OPENAI_API_KEY[/red]")
        console.print("[yellow]请设置环境变量：export OPENAI_API_KEY='your-api-key'[/yellow]")
        sys.exit(1)
    
    # 创建 AI Writer 实例
    writer = AIWriter(model="gpt-4o", temperature=0.7)
    
    console.print("\n[green]✅ AI 写作引擎已就绪！[/green]\n")
    
    # 简单演示
    try:
        result = writer.generate("用一句话介绍你自己")
        console.print(Panel(result, title="✨ AI 回复", border_style="green"))
    except Exception as e:
        console.print(f"[red]❌ 错误：{e}[/red]")


if __name__ == "__main__":
    main()
