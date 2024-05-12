from vanna.chromadb import ChromaDB_VectorStore
from vanna.openai import OpenAI_Chat

from vanna_demo.config import my_config


class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config, chroma_config=None):
        ChromaDB_VectorStore.__init__(self, config=chroma_config)
        OpenAI_Chat.__init__(self, config={ 'api_key': config.openai_api_key })


vn = MyVanna(my_config, dict(path=my_config.chroma_path))
vn.connect_to_postgres(
    host=my_config.db_host,
    dbname=my_config.db_name,
    user=my_config.db_user,
    password=my_config.db_pass,
    port=my_config.db_port,
)
