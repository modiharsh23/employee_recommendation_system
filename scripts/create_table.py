import sys
import os

# Add the parent folder to path so we can import app.db
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db import get_db_connection

def create_schema():
    conn = get_db_connection()
    if not conn:
        return
    
    cur = conn.cursor()
    
    print("⏳ Creating 'employees' table...")
    
    # 1. Enable Extension (just in case)
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    
    # 2. Drop table if exists (Clean slate for development)
    cur.execute("DROP TABLE IF EXISTS employees;")
    
    # 3. Create Table
    # Note: embedding vector(384) matches our NLP model size
    create_table_query = """
    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(100),
        role VARCHAR(100),
        skills TEXT,
        experience_years INT,
        bio TEXT,
        embedding vector(384)
    );
    """
    cur.execute(create_table_query)
    
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Table 'employees' created successfully with Vector support!")

if __name__ == "__main__":
    create_schema()