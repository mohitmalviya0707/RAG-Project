from langchain_community.document_loaders import TextLoader



data = TextLoader("document loders/notes.txt")


print (data)

docs = data.load()
print(docs[0])