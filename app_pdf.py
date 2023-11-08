import logging
import sys

from llama_index import ServiceContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms import OpenAI

from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.query_engine import SubQuestionQueryEngine

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


mastercard_docs = SimpleDirectoryReader(
    input_files=["./data/mastercard-10k-2021.pdf"]
).load_data()
visa_docs = SimpleDirectoryReader(
    input_files=["./data/visa-10k-2021.pdf"]
).load_data()

mastercard_index = VectorStoreIndex.from_documents(mastercard_docs)
visa_index = VectorStoreIndex.from_documents(visa_docs)

mastercard_engine = mastercard_index.as_query_engine(similarity_top_k=3)
visa_engine = visa_index.as_query_engine(similarity_top_k=3)

query_engine_tools = [
    QueryEngineTool(
        query_engine=mastercard_engine,
        metadata=ToolMetadata(
            name="mastercard_10k",
            description=(
                "Provides information about Mastercard financials for year 2021"
            ),
        ),
    ),
    QueryEngineTool(
        query_engine=visa_engine,
        metadata=ToolMetadata(
            name="visa_10k",
            description=(
                "Provides information about Visa financials for year 2021"
            ),
        ),
    ),
]


s_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=query_engine_tools
)

while True:
    print("################################################")
    user_input = input("Ask about pdfs:\n")
    response = s_engine.query(user_input)
    print("################################################")
    print(response)
    print("################################################")
