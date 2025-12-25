import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            os.getenv("DATABASE_URL"), # We will use just one URL variable now
            sslmode='require'          # <--- IMPORTANT for cloud DBs
        )
        return conn
    except Exception as e:
        print(f"❌ Database Connection Failed: {e}")
        return None