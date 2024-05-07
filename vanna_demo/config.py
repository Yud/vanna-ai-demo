import os

from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(dotenv_path=find_dotenv(), override=True)  # read local .env file


class MyConfig:
    def __init__(self):
        self.init()

    def init(self):
        self.gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
        self.gemini_model: str = os.getenv("GEMINI_MODEL", "")
        self.db_host: str = os.getenv("DB_HOST", "localhost")
        self.db_name: str = os.getenv("DB_NAME", "")
        self.db_pass: str = os.getenv("DB_PASS", "")
        self.db_user: str = os.getenv("DB_USER", "")
        self.db_port: str = os.getenv("DB_PORT", "5432")


my_config = MyConfig()
