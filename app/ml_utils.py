from sentence_transformers import SentenceTransformer
import numpy as np

# Load the model once when this script is imported
# 'all-MiniLM-L6-v2' is small (80MB) and fast
print("⏳ Loading NLP Model (this may take a moment)...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Model loaded successfully!")

def get_embedding(text):
    """
    Converts a text string into a list of floating point numbers (vector).
    """
    # The model returns a numpy array, we convert to list for the database
    vector = model.encode(text)
    return vector.tolist()

# --- Test Block (Runs only if you execute this file directly) ---
if __name__ == "__main__":
    test_text = "Senior Python Developer with AI experience"
    vector = get_embedding(test_text)
    
    print(f"\nTest Sentence: '{test_text}'")
    print(f"Vector Length: {len(vector)} (Should be 384)")
    print(f"First 5 dimensions: {vector[:5]}...")