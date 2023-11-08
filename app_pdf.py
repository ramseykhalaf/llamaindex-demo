import argparse
import os

from llama_index import VectorStoreIndex, SimpleDirectoryReader, load_index_from_storage, StorageContext, ServiceContext
from llama_index.llms import OpenAI
from llama_index.query_engine import SubQuestionQueryEngine
from llama_index.tools import QueryEngineTool, ToolMetadata


# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

def parse_args():
    parser = argparse.ArgumentParser()
    return parser.parse_args()

def do_stuff(args):

    llm = OpenAI(temperature=0, model="text-davinci-003", max_tokens=-1)
    service_context = ServiceContext.from_defaults(llm=llm)

    storage_base = '/usr/src/storage/app_pdf'
    storage_mastercard = '/usr/src/storage/app_pdf/mastercard'
    storage_visa = '/usr/src/storage/app_pdf/visa'

    if not os.path.exists(os.path.join(storage_base)):
        mastercard_docs = SimpleDirectoryReader(
            input_files=["./data/mastercard/mastercard-10q-2023q2.pdf"]
        ).load_data()
        visa_docs = SimpleDirectoryReader(
            input_files=["./data/visa/visa-10q-2023q2.pdf"]
        ).load_data()

        service_context = ServiceContext.from_defaults(chunk_size=512)

        mastercard_index = VectorStoreIndex.from_documents(mastercard_docs, service_context=service_context)
        visa_index = VectorStoreIndex.from_documents(visa_docs, service_context=service_context)

        print("################################################")
        print('Creating persistent index storage...')
        print("################################################")
        mastercard_index.storage_context.persist(persist_dir=storage_mastercard)
        visa_index.storage_context.persist(persist_dir=storage_visa)
        print("################################################")
        print('Done')
        print("################################################")

    else:
        print("################################################")
        print('Loading existing: building storage context...')
        print("################################################")
        mastercard_storage_context = StorageContext.from_defaults(persist_dir=storage_mastercard)
        visa_storage_context = StorageContext.from_defaults(persist_dir=storage_visa)
        print("################################################")
        print('Done')
        print("################################################")

        print("################################################")
        print('Loading existing: loading index...')
        print("################################################")
        mastercard_index = load_index_from_storage(mastercard_storage_context)
        visa_index = load_index_from_storage(visa_storage_context)
        print("################################################")
        print('Done')
        print("################################################")

    mastercard_engine = mastercard_index.as_query_engine(similarity_top_k=4)
    visa_engine = visa_index.as_query_engine(similarity_top_k=4)

    query_engine_tools = [
        QueryEngineTool(
            query_engine=mastercard_engine,
            metadata=ToolMetadata(
                name="mastercard_10k",
                description=(
                    "Provides information about Mastercard financials for the quarter Q2 2022"
                ),
            ),
        ),
        QueryEngineTool(
            query_engine=visa_engine,
            metadata=ToolMetadata(
                name="visa_10k",
                description=(
                    "Provides information about Visa financials for the quarter Q2 2022"
                ),
            ),
        ),
    ]

    while True:
        print("################################################")
        s_engine = SubQuestionQueryEngine.from_defaults(
            query_engine_tools=query_engine_tools
        )
        user_input = input("Ask about pdfs:\n")
        response = s_engine.query(user_input)
        print("################################################")
        print(response)
        print("################################################")


def main():
    args = parse_args()
    do_stuff(args)

if __name__ == '__main__':
    main()