from typing import Any

from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


class Base(object):
    @classmethod
    def run_demo(cls, input: dict[str, Any] = None):
        pass


class BaseDemo(Base):
    @classmethod
    def run_demo(cls, input: dict[str, Any] = None):
        """
        base demo
        :param input:
        :return:
        """
        '''
        提示词模板 
        '''
        prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
        '''
        使用llm openai_api_base是代理 api_key是gpt的key
        '''
        # llm = ChatOpenAI(api_key=self.api_key, openai_api_base=self.openai_api_base)
        llm = ChatOpenAI()
        '''
        output_parser 是处理输出返回结果
        '''
        output_parser = StrOutputParser()

        '''
        chain 是一个不同组件拼装的一个链，|是将上一个组件的结果当做参数传递给下一个组件 
        chain这个链路是先组装prompt->调用llm->输出结果
        '''
        chain = prompt | llm | output_parser
        resp_msg = chain.invoke(input=input)
        print(resp_msg)
        '''
        resp_msg:
           Why did the scarecrow adopt a dog?

           Because he needed a "barking" buddy!
        '''
