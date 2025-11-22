"""
From https://github.com/dhilmathy/TfL-python-api
"""

from tfl.client import Client
from tfl.api_token import ApiToken
import dotenv
import os

dotenv.load_dotenv()

token = ApiToken(os.getenv("app_id"), os.getenv("app_key"))

client = Client(token)
print(client.get_line_meta_modes())
print(client.get_lines(mode="bus")[0])
print(client.get_lines(line_id="victoria")[0])
