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

