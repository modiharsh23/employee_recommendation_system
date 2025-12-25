import sys
import os
import pandas as pd

# 1. Setup path to import from 'app' folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db import get_db_connection
from app.ml_utils import get_embedding
from scripts.preprocess import load_and_process_data

def ingest_data():
    # Load the dataframe with the 'combined_text' column already prepared
    print("📂 Loading data...")
    df = load_and_process_data()
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    print(f"🚀 Starting ingestion of {len(df)} rows into PostgreSQL...")
    
    for index, row in df.iterrows():
        # 2. Generate the Vector (The "AI" part)
        embedding = get_embedding(row['combined_text'])
        
        # 3. Insert into DB
        insert_query = """
        INSERT INTO employees 
        (full_name, role, skills, experience_years, bio, embedding)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        cur.execute(insert_query, (
            row['full_name'],
            row['role'],
            row['skills'],
            row['experience_years'],
            row['bio'],
            embedding  # The list of 384 numbers goes here
        ))
        
        # Simple progress indicator
        if (index + 1) % 5 == 0:
            print(f"   Processed {index + 1}/{len(df)} rows...")

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data Ingestion Complete!")

if __name__ == "__main__":
    ingest_data()