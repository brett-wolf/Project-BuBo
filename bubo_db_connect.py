import os
import psycopg
from psycopg.rows import dict_row

# Use DATABASE_URL from environment (Render provides this)
DATABASE_URL = os.environ.get("BUBO_DB_CONNECTIONSTRING")

def get_connection():
    """Create a new psycopg connection to the database using URL."""
    print(DATABASE_URL)
    #return psycopg.connect(DATABASE_URL, row_factory=dict_row)

get_connection()