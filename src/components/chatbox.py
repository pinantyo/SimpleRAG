import os
from decouple import config
from groq import Groq
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ["GROQ_API_KEY"] = config("GROQ_API")

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

class DocLoader:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    def __call__(self, ):
        docs = TextLoader().load()
        return self.splitter.split_documents(docs)

class Model:
    def __init__(self):
        self.client = ChatGroq(model=config("MODEL"))

    def __call__(self, *args, **kwds):
        pass

class Embedding:
    def __init__(self):
        self.client = HuggingFaceEmbeddings(model_name=config("EMBEDDING"))

    def __call__(self, documents):
        embedding = self.client.embed_documents(documents)

class VectorSpace:
    def __init__(self, embedding_client):
        self.client = InMemoryVectorStore(embedding_client)

    def __call__(self, query):
        pass

