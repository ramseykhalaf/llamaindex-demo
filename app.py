import os.path
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import logging
import sys
#
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


############################


from llama_index.agent import OpenAIAgent
import openai

# Import and initialize our tool spec
from llama_hub.tools.wikipedia.base import WikipediaToolSpec
from llama_index.tools.tool_spec.load_and_search.base import LoadAndSearchToolSpec

# RSSNewsReader = download_loader("RssReader")

wiki_spec = WikipediaToolSpec()
# Get the search wikipedia tool
tool = wiki_spec.to_tool_list()[1]
# Create the Agent with our tools
chat_engine = OpenAIAgent.from_tools(
    LoadAndSearchToolSpec.from_defaults(tool).to_tool_list(), verbose=True
)

while True:
    print("################################################")
    user_input = input("Chat with wikipedia:\n")
    response = chat_engine.chat(user_input)
    print("################################################")
    print(response)
    print("################################################")


####################################

# storage = '/usr/src/storage'
#
# if not os.path.exists(os.path.join(storage, 'vector_store.json')):
#
#     # create the index
#     documents = SimpleDirectoryReader('data').load_data()
#     index = VectorStoreIndex.from_documents(documents)
#     # store it for later
#     print('Creating persistent index storage...')
#     index.storage_context.persist(persist_dir=storage)
#     print('Done')
# else:
#     # load the existing index
#     print('Loading existing: building storage context...')
#     storage_context = StorageContext.from_defaults(persist_dir=storage)
#     print('Done')
#
#     print('Loading existing: loading index...')
#     index = load_index_from_storage(storage_context)
#     print('Done')
#
#
# query_engine = index.as_query_engine()
# response = query_engine.query("What did the author do growing up?")
# print(response)

# storage = '/usr/src/storage'
#
# if not os.path.exists(os.path.join(storage, 'vector_store.json')):
#
#     # create the index
#     documents = SimpleDirectoryReader('data').load_data()
#     index = VectorStoreIndex.from_documents(documents)
#     # store it for later
#     print('Creating persistent index storage...')
#     index.storage_context.persist(persist_dir=storage)
#     print('Done')
# else:
#     # load the existing index
#     print('Loading existing: building storage context...')
#     storage_context = StorageContext.from_defaults(persist_dir=storage)
#     print('Done')
#
#     print('Loading existing: loading index...')
#     index = load_index_from_storage(storage_context)
#     print('Done')
#
#
#################################
# from pathlib import Path
# from llama_index import download_loader
#
# SimpleCSVReader = download_loader("SimpleCSVReader")
#
# loader = SimpleCSVReader(encoding="utf-8")
# documents = loader.load_data(file=Path('./finance.csv'))
#
# index = VectorStoreIndex.from_documents(documents)
#
# query_engine = index.as_query_engine()
#
# response = query_engine.query("What is the country with the most sales")
# print(response)


############################

# from llama_index import download_loader
#
# RSSNewsReader = download_loader("RssReader")
# reader = RSSNewsReader()
# urls = [
#     "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
# ]
#
# documents = reader.load_data(urls=urls)
#
# index = VectorStoreIndex.from_documents(documents)
#
# chat_engine = index.as_chat_engine()
#
# while True:
#     print("################################################")
#     user_input = input("Ask about the NYT news:\n")
#     response = chat_engine.chat(user_input)
#     print("################################################")
#     print(response)
#     print("################################################")

