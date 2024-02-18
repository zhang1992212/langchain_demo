from typing import Any

from demo.base import Base
from langchain_community.vectorstores import DocArrayInMemorySearch,FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings


class RagSearch(Base):
    @classmethod
    def run_demo(cls, input: dict[str, Any] = None):
        """
        run_demo
        :return:
        """
        vectorstore = DocArrayInMemorySearch.from_texts(
            ["harrison worked at kensho", "bears like to eat honey"],
            embedding=OpenAIEmbeddings(),
        )

        vectorstore = FAISS.from_texts(
            ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
        )
        retriever = vectorstore.as_retriever()

        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        model = ChatOpenAI()
        output_parser = StrOutputParser()

        # setup_and_retrieval = RunnableParallel(
        #     {"context": retriever, "question": RunnablePassthrough()}
        # )

        setup_and_retrieval = {"context": retriever, "question": RunnablePassthrough()}

        chain = setup_and_retrieval | prompt | model | output_parser
        resp_msg = chain.invoke("where did harrison work?")
        print(resp_msg)
