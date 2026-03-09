"""AI 写作工具 - 核心写作引擎"""

from typing import Optional, List
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class AIWriter:
    """AI 写作核心类"""
    
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    
    def generate(self, prompt: str) -> str:
        """生成文本内容"""
        chain = ChatPromptTemplate.from_messages([
            ("system", "你是一个专业的 AI 写作助手。请根据用户的请求，创作高质量的内容。"),
            ("user", prompt)
        ]) | self.llm | StrOutputParser()
        
        return chain.invoke({})
    
    def rewrite(self, text: str, style: str = "professional") -> str:
        """重写文本"""
        prompt = f"""请帮我重写以下文本，要求使用 {style} 风格：

{text}"""
        return self.generate(prompt)
    
    def summarize(self, text: str, max_length: int = 500) -> str:
        """总结文本"""
        prompt = f"""请总结以下文本，控制在 {max_length} 字以内：

{text}"""
        return self.generate(prompt)


if __name__ == "__main__":
    writer = AIWriter()
    result = writer.generate("写一首关于春天的诗")
    print(result)
