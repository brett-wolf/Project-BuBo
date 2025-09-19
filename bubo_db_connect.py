import os
import psycopg
from psycopg.rows import dict_row

# Use DATABASE_URL from environment (Render provides this)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://bhowells:o2NJjZoRqS8IqrZHUjAFO1ChtUraujGW@dpg-d366h83ipnbc73akr66g-a.virginia-postgres.render.com/bubodb")

def get_connection():
    """Create a new psycopg connection to the database using URL."""
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)