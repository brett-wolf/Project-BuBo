import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()
# Use DATABASE_URL from environment (Render provides this)
DATABASE_URL = os.getenv("BUBO_DB_CONNECTIONSTRING")

def get_connection():
    """Create a new psycopg connection to the database using URL."""
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)