import os
import streamlit as st
from decouple import config
from groq import Groq
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader, PyPDFLoader
# from langchain_core.vectorstores import InMemoryVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from data.ops import ContextDB

os.environ["GROQ_API_KEY"] = config("GROQ_API")

# Datatype
class Dictionary:
    def __init__(self, dictionary):
        self._dict = dictionary

    def __getattr__(self, name):
        if name in self._dict:
            return self._dict[name]
        else:
            raise AttributeError(f"'Dictionary' object has no attribute '{name}'")
    

class ChatBot:
    def __init__(self, max_length: int = 128):
        self.client = Groq(
            # This is the default and can be omitted
            api_key=config("GROQ_API"),
        )
        self.max_length = max_length

    def text_similarity(self, query, context):
        pass
    
    def interact(self, query):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant."
                },{
                    "role": "user",
                    "content": query,
                }
            ],
            model=config("MODEL"),
        )

        return chat_completion.choices[0].message.content

class RAGCreation:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.client = HuggingFaceEmbeddings(model_name=config("EMBEDDING"))
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.model = ChatGroq(model=config("MODEL"))

    def document_loader(self, documents: list):
        # docs = TextLoader(documents).load() # only for .txt
        
        # Load PDF
        docs_content = []
        for index, i in enumerate(documents):
            loader = PyPDFLoader(i)
            docs_content.extend(loader.load())

        return self.splitter.split_documents(docs_content)

    def vector_creation(self, documents):
        embedding = FAISS.from_documents(documents, self.client)
        return embedding

    def rag_pipeline(self, documents: list):
        documents = self.document_loader(documents)
        embedding = self.vector_creation(documents)
        retriever = embedding.as_retriever()
        self.rag = RetrievalQA.from_llm(
            llm=self.model,
            retriever=retriever
        )
    
    def interact(self, query):
        return self.rag.invoke(query)