# 🚀 AI Employee Recommendation System

An intelligent search engine that uses **Natural Language Processing (NLP)** and **Vector Similarity Search** to find the perfect candidate based on a job description.

Unlike keyword matching, this system understands *context*. Searching for "Marketing expert" will return candidates with "SEO" or "Content Strategy" skills even if the exact word "Marketing" isn't present.

![Project Demo](employee-recommender-nlp/demo_screenshot.png)

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI
* **AI/ML:** Sentence-Transformers (Hugging Face), PyTorch
* **Database:** PostgreSQL + `pgvector` (Vector Database)
* **Frontend:** React, Vite, Axios
* **Containerization:** Docker (Optional)

## ⚡ Features
* **Semantic Search:** Converts text queries into 384-dimensional vectors.
* **Vector Database:** Stores employee embeddings in PostgreSQL for millisecond-latency retrieval.
* **Real-time Matching:** Calculates Cosine Similarity to rank candidates by relevance.
* **Modern UI:** Dark-mode React interface with match percentage indicators.

## 🏃‍♂️ How to Run Locally

### 1. Database Setup
Ensure you have PostgreSQL installed with the `pgvector` extension.
```bash
# Create database
createdb employee_db
# Enable extension inside psql
CREATE EXTENSION vector;
```

### 2. Backend Setup
```bash
cd employee-recommender-nlp
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt

# Run the data pipeline (Ingest mock data + Vectorize)
python scripts/create_table.py
python scripts/ingest_data.py

# Start the API
python -m uvicorn app.main:app --reload
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 4. API endpoints
| Method | Endpoint | Description |
| --- | --- | --- |
| GET | / | Health check |
| POST | /search | "Accepts {""query"": ""...""} and returns top 5 matches" |

### 5. Future Improvements
- Add filters for "Years of Experience" alongside vector search.
- Implement Resume Parsing (PDF to Text) for auto-ingestion.
- Deploy to AWS using Docker Containers.