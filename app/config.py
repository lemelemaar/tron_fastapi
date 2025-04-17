from tronpy import Tron
from tronpy.providers import HTTPProvider
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("TRON_API_KEY")

client = Tron(HTTPProvider(api_key=api_key))

DATABASE_URL = os.getenv("DATABASE_URL")
