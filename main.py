from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load env variables
load_dotenv()

# Load LLM
llm = ChatMistralAI(model="mistral-small-2506")

# Load document
loader = TextLoader("document loaders/notes.txt")
docs = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

# Prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that summarizes text."),
    ("human", "{data}")
])

# Process each chunk
for chunk in chunks:
    prompt = template.format_messages(data=chunk.page_content)
    response = llm.invoke(prompt)
    
    print(response.content)
    print("------") ........................
