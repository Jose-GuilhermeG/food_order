from logging import INFO
from os import getenv as env
from os.path import join
from pathlib import Path

from dotenv import load_dotenv

#base settings
BASE_DIR = Path(__file__).absolute().parent.parent.parent.parent
DOT_ENV_PATH = join(BASE_DIR , '.env')

load_dotenv(DOT_ENV_PATH)

# Application settings
DEBUG = env("DEBUG")

#database
DATABASE_ENGINE = env("DATABASE_ENGINE")
DATABASE_USER = env("DATABASE_USER")
DATABASE_PASSWORD = env("DATABASE_PASSWORD")
DATABASE_HOST = env("DATABASE_HOST")
DATABASE_PORT = env("DATABASE_PORT")
DATABASE_NAME = env("DATABASE_NAME")
DATABASE_URI = f"{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

#STATIC_DATA
MEDIA_DIR = join(BASE_DIR , "src" , "api" , "adapters" , "static")
MEDIA_PREFIX = "/static/"
MEDIA_ROOT = f"http://localhost:8000{MEDIA_PREFIX}"

#Cache
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
REDIS_PASSWORD = env("REDIS_PASSWORD")

#loggin
LOGIN_LEVEL=INFO
LOG_FILE_NAME="system_loggin.log"
LOG_FILE = join(BASE_DIR , LOG_FILE_NAME)
