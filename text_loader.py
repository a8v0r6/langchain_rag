from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template= "Summarize the following. {text} ",
    input_variables= ['text'],
)

parser = StrOutputParser()

model = ChatOpenAI()

loader = TextLoader('sample.txt', encoding='utf-8')

docs = loader.load()

# print(type(docs))

# print(len(docs))

# print(docs[0].page_content)

chain = prompt | model | parser

res = chain.invoke({'text': docs[0].page_content})

print(res)