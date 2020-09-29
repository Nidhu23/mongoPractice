from environs import Env
from pymongo import MongoClient
env = Env()
env.read_env()
client = MongoClient(
    host=env("host"),
    port=27017,
    username=env("username"),
    password=env("password"),
)