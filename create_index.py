import os
with open('api_key.txt') as f:
    key = f.read().strip()
    os.environ["OPENAI_API_KEY"] = key

from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index import download_loader

CJKPDFReader = download_loader("CJKPDFReader")
loader = CJKPDFReader()

service_context = ServiceContext.from_defaults(chunk_size=512)
documents = loader.load_data("scala_text.pdf")
index = VectorStoreIndex.from_documents(
    documents,
    service_context=service_context
)
index.storage_context.persist()
