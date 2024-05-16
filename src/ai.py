import os
from abc import abstractmethod, ABC

from langchain_community.chat_models.edenai import ChatEdenAI
from langchain_core.messages import HumanMessage


class BaseLLMManager:

    @abstractmethod
    def generate_text(self, prompt):
        raise NotImplementedError

class LLMManager(BaseLLMManager, ABC):
    def __init__(self):
        self.llm_model = ChatEdenAI(
            edenai_api_key=os.getenv("AI_API_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTVhMjhhZGQtMjEwZS00NDU5LTk3ZGItMTc2ODVlYWI4YmMyIiwidHlwZSI6ImFwaV90b2tlbiJ9.Xs8aPZyVgWj0WaDiSjXY3u3Zni9S_zFz_rT2s_El72c"),
            provider="openai",
            temperature=0.2,
            max_tokens=250,
            fallback_providers="google")
        # This key public, that's why I didn't hide it in env, also for make extend project easier.

    def generate(self, prompt: str) -> str:
        return self.llm_model.generate([[HumanMessage(
            f"generate information about: {prompt}")]]
        ).dict().get("generations")[0][0].get("text")

