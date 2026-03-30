from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document  

load_dotenv()      
   

docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

# Embedding model
embedding_model = OpenAIEmbeddings()     

# Vector DB
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma-db"
)

# Similarity search
result = vectorstore.similarity_search("what is used for data analysis", k=2)

print("🔍 Similarity Search Results:")
for r in result:
    print(r.page_content)

# Retriever
retriever = vectorstore.as_retriever()

retrieved_docs = retriever.invoke("explain deep learning")

print("\n📚 Retriever Results:")
for d in retrieved_docs:
    print(d.page_content)
