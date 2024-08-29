from app.core.ai_service import AIService


class LangChainService(AIService):
    async def process_prompt(self, prompt: str) -> str:
        # Implement LangChain logic here
        pass
