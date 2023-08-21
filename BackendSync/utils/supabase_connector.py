import requests
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_HEADERS = {
    "apikey": os.getenv("SUPABASE_API_KEY"),
    "Content-Type": "application/json"
}

def update_supabase(topic, name, author):
    payload = {
        "topic": topic,
        "name": name,
        "author": author
    }

    response = requests.post(SUPABASE_URL, headers=SUPABASE_HEADERS, json=payload)

    return response.json()
