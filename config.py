import os
from dotenv import load_dotenv


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self, load_from_file=True):

        self.RUN_MODE = os.environ.get("RUN_MODE", "DEBUG")


