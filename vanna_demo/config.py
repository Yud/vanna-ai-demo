import os
from pathlib import Path


from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(dotenv_path=find_dotenv(), override=True)  # read local .env file

class MyConfig:
    def __init__(self):
        self.init()

    def init(self):
        path = Path(".")
        ROOT_DIR = path.parent.absolute()

        self.gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
        self.gemini_model: str = os.getenv("GEMINI_MODEL", "")
        self.openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
        self.db_host: str = os.getenv("DB_HOST", "localhost")
        self.db_name: str = os.getenv("DB_NAME", "")
        self.db_pass: str = os.getenv("DB_PASS", "")
        self.db_user: str = os.getenv("DB_USER", "")
        self.db_port: str = os.getenv("DB_PORT", "5432")
        self.chroma_path = f"{ROOT_DIR}/chromadb_data/"
        self.root_dir = ROOT_DIR


my_config = MyConfig()
