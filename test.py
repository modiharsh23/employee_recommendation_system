import psycopg2

# Update these details with your local postgres setup
# Default password often is 'postgres' or empty string
conn = psycopg2.connect(
    dbname="employee_db",
    user="postgres",
    password="harsh@2359", 
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Try to run a vector command
try:
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    print("✅ Success! Connected to DB and pgvector is ready.")
except Exception as e:
    print(f"❌ Error: {e}")

cur.close()
conn.close()