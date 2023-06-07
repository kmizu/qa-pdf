import os

with open('api_key.txt') as f:
    key = f.read().strip()
    os.environ["OPENAI_API_KEY"] = key

from llama_index import StorageContext, load_index_from_storage
from llama_index import LLMPredictor
from langchain.chat_models import ChatOpenAI

storage_context = StorageContext.from_defaults(persist_dir='./storage')
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine(llm = ChatOpenAI(temperature = 0, model_name="gpt-3.5-turbo"))

while True:
    line = input("質問: ")
    if line.strip() == "exit": 
        break
    response = query_engine.query(line)
    print("回答： " + str(response))
