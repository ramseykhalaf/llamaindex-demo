from llama_index import download_loader
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

PubmedReader = download_loader("PubmedReader")
loader = PubmedReader()

topic = input("Enter topic to search for papers on pubmed (e.g. melanoma):\n")
documents = loader.load_data(search_query=topic)

index = VectorStoreIndex.from_documents(documents)

chat_engine = index.as_chat_engine()

while True:
    print("################################################")
    user_input = input(f'Ask about {topic}:\n')
    response = chat_engine.chat(user_input)
    print("################################################")
    print(response)
    print("################################################")

