from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from typing import List
from pydantic import BaseModel

from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.prompts import PromptTemplate
import os
import re
import json

app = FastAPI()

# 允许所有来源
origins = [
    "null",
    "https://www.bluelskj.com",
    "http://aitools.chuheng.tech"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = "sk"
openai_api_key = OPENAI_API_KEY

print("OpenAI API Key:", openai_api_key)

# 提示词
prompt_template = """
使用以下的上下文来回答最后的问题。 \
最多用三句话，回答要尽可能简明扼要。\
在回答的最后一定要说"或许你可以试试下面的工具".
{context}
Question: {question}
Helpful Answer:
"""


QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt_template)

# 加载数据
""" 嵌入markdown
loader = UnstructuredMarkdownLoader(
    "./data/AI大学堂.md", mode="elements", strategy="fast",
)
"""
loader = DirectoryLoader('/home/code/blueshirt/AI_Search/data/',
                         glob="**/*.md", show_progress=True, use_multithreading=False)
docs = loader.load()

print(f"文档个数：\n", len(docs))


# 文本分割
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(docs)

# 向量数据库存储
vectorstore = Chroma.from_documents(
    documents=all_splits, embedding=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))


# 生成
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,
                 openai_api_key=OPENAI_API_KEY)
qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=vectorstore.as_retriever(),
                                       return_source_documents=True,
                                       chain_type_kwargs={
                                           "prompt": QA_CHAIN_PROMPT}
                                       )


# 获取title
def getTitle(doc_metadata_source):
    match = re.search(r"/data/(.*).md", doc_metadata_source)
    wp_title = match.group(1) if match else None

    return wp_title


json_path = "title2url.json"
json_data = None
with open(json_path, 'r', encoding="utf-8") as json_file:
    json_data = json.load(json_file)


def getURL(post_title):
    return json_data.get(post_title, None)


# 定义帖子类型
class PostData(BaseModel):
    post_title: str
    post_url: str


# 定义请求和响应模型
class QueryModel(BaseModel):
    query: str


class ResponseModel(BaseModel):
    result: str
    post_data: List[PostData]


@app.post("/ask", response_model=ResponseModel)
async def ask_question(query: QueryModel):
    result = qa_chain(query.dict())

    post_data_list = []
    for post in result["source_documents"]:
        print(post)
        print(post.metadata)
        print(post.page_content)
        post_data_list.append({
            "post_title": getTitle(post.metadata["source"]),
            "post_url": getURL(getTitle(post.metadata["source"]))
        })
        print(post_data_list)

    return {
        "result": result["result"],
        "post_data": post_data_list
    }


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 使用相似性搜索检索任何问题的相关拆分。
"""
question = "我的代码有问题"
print(question)
docs = vectorstore.similarity_search(question)
len(docs)

result = qa_chain({"query": question})

print(result["result"])
print(result["source_documents"])
"""
