import os
from dotenv import load_dotenv

load_dotenv()

API_CLIENT_ID = os.getenv("API_CLIENT_ID")
API_CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")
API_USER_AGENT = os.getenv("API_USER_AGENT")
SUBREDDIT_NAME = os.getenv("SUBREDDIT_NAME")
START_DATE = os.getenv("START_DATE")
END_DATE = os.getenv("END_DATE")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "data/raw/laptop_comments.json")