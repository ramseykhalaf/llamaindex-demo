from llama_index import VectorStoreIndex
from llama_index import download_loader

RSSNewsReader = download_loader("RssReader")
reader = RSSNewsReader()
urls = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
]

documents = reader.load_data(urls=urls)

index = VectorStoreIndex.from_documents(documents)

chat_engine = index.as_chat_engine()

while True:
    print("################################################")
    user_input = input("Ask about the NYT news:\n")
    print("################################################")

    response = chat_engine.chat(user_input)

    print("================================================")
    print(response)
    print("================================================")

