import os
import requests
import psycopg2
from psycopg2.extras import execute_values

# 🔑 Load your Watchmode API key (set as an environment variable for safety)
WATCHMODE_API_KEY = os.getenv("WATCHMODE_API_KEY")

# 🔌 Database connection string (from Render dashboard)
DATABASE_URL = os.getenv("DATABASE_URL")

# --- API functions ---
BASE_URL = "https://api.watchmode.com/v1"

def fetch_genres():
    url = f"{BASE_URL}/genres/?apiKey={WATCHMODE_API_KEY}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()