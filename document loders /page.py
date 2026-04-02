from langchain_community.document_loaders import WebBaseLoader

url = "//wensite url "

data = WebBaseLoader(url)

docs = data.load()

print (docs[0].page_content)


1234457688997


