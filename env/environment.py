import os
from dotenv import load_dotenv


class Environment:
    def __init__(self, path: str = "/.env"):
        self.get_file_env(path)

    def get_file_env(self, path: str):
        self.reload(os.getcwd() + path)

    def reload(self, env_path: str):
        load_dotenv(dotenv_path=env_path)
