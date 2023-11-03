import os.path
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import logging
import sys

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

storage = '/usr/src/storage'

if not os.path.exists(os.path.join(storage, 'vector_store.json')):

    # create the index
    documents = SimpleDirectoryReader('data').load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    print('Creating persistent index storage...')
    index.storage_context.persist(persist_dir=storage)
    print('Done')
else:
    # load the existing index
    print('Loading existing: building storage context...')
    storage_context = StorageContext.from_defaults(persist_dir=storage)
    print('Done')

    print('Loading existing: loading index...')
    index = load_index_from_storage(storage_context)
    print('Done')


query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
