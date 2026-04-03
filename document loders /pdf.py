from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


data = PyMuPDFLoader("dacument loder / GRU.pdf")

docs = data.load()

Splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap =10,
)

print(docs)  
