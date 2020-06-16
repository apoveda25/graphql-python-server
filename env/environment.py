import os
from dotenv import load_dotenv


class Environment:
    def __init__(self, path: str = None):
        if "APP_ENV" not in os.environ:
            self.get_file_env(path)
        else:
            if os.environ["APP_ENV"] is "DEVELOPMENT":
                self.get_file_env(path)

    def get_file_env(self, path: str):
        if path == None:
            env_path = os.getcwd() + "/.env"
        else:
            env_path = os.getcwd() + path
        self.reload(env_path)

    def reload(self, env_path: str):
        load_dotenv(dotenv_path=env_path)
