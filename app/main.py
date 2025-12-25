from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.db import get_db_connection
from app.ml_utils import get_embedding
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Employee Recommender")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow your React app
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (POST, GET, etc.)
    allow_headers=["*"],
)

# Define the input format
class SearchRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "System is running. Go to /docs to test the search."}

@app.post("/search")
def search_employees(request: SearchRequest):
    # 1. Edge Case: Handle Empty Queries (Day 8 Fix)
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query text cannot be empty")

    # 2. Convert text to vector
    query_vector = get_embedding(request.query)
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # 3. SQL Query - Tuned Limit to 10 (Day 8 Fix)
    search_sql = """
    SELECT id, full_name, role, experience_years, bio, 
           (embedding <=> %s) as distance
    FROM employees
    ORDER BY distance ASC
    LIMIT 10;  -- Increased from 5 to 10
    """
    
    cur.execute(search_sql, (str(query_vector),))
    results = cur.fetchall()
    
    conn.close()
    
    response = []
    for row in results:
        similarity_score = 1 - row[5] 
        
        response.append({
            "id": row[0],
            "name": row[1],
            "role": row[2],
            "experience": row[3],
            "bio_snippet": row[4][:150] + "...", # Increased snippet length slightly
            "similarity_score": round(similarity_score, 2)
        })
        
    return response