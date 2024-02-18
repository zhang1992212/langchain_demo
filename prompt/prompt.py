from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompt_values import PromptValue


class Prompt:
    api_key: str
    openai_api_base: str

    def __init__(self, api_key: str, openai_api_base: str):
        self.api_key = api_key
        self.openai_api_base = openai_api_base

    @classmethod
    def get_prompt(cls, template: str, value: dict) -> ChatPromptTemplate:
        prompt = ChatPromptTemplate.from_template(template)
        prompt_value = prompt.invoke(value)
        print("to_messages:", prompt_value.to_messages())
        print("to_string:", prompt_value.to_string())
        return prompt
