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

OPENAI_API_KEY = "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"
#openai_api_key = os.environ.get("OPENAI_API_KEY")
openai_api_key = OPENAI_API_KEY

print("OpenAI API Key:", openai_api_key)


""" 嵌入markdown
loader = UnstructuredMarkdownLoader(
    "./data/AI大学堂.md", mode="elements", strategy="fast",
)
"""

# 提示词
prompt_template="""
使用以下的上下文来回答最后的问题。 \
最多用三句话，回答要尽可能简明扼要。\
在回答的最后一定要说"或许你可以试试下面的工具".
{context}
Question: {question}
Helpful Answer:
"""


QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt_template)

#加载数据
loader = DirectoryLoader('./data/', glob="**/*.md", show_progress=True, use_multithreading=True)
docs = loader.load()

print(f"文档个数：%\n", len(docs))


#文本分割
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
all_splits = text_splitter.split_documents(docs)

# 向量数据库存储
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings(openai_api_key= OPENAI_API_KEY))

# 使用相似性搜索检索任何问题的相关拆分。
question = "我的代码有问题"
print(question)
docs = vectorstore.similarity_search(question)
len(docs)

#生成
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)
qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=vectorstore.as_retriever(),
                                       return_source_documents=True,
                                       chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

result = qa_chain({"query": question})

print(result["result"])
print(result["source_documents"])




