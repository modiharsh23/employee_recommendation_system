import pandas as pd
import os

# Define file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'employee.csv')

def load_and_process_data():
    if not os.path.exists(CSV_PATH):
        print(f"Error: File not found at {CSV_PATH}")
        return None

    # Load Data
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded {len(df)} rows from CSV.")

    # Create 'combined_text' column
    # We mix the Role, Skills, and Bio so the AI sees all context
    df['combined_text'] = df.apply(
        lambda row: f"Role: {row['role']}. Skills: {row['skills']}. Bio: {row['bio']}", axis=1
    )

    # Preview the first row
    print("\n--- Example Processed Data ---")
    print(df['combined_text'].iloc[0])
    
    return df

if __name__ == "__main__":
    load_and_process_data()