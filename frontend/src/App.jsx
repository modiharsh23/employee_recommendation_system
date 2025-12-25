import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSearch = async () => {
    if (!query) return;
    
    setLoading(true);
    setError(null);

    try {
      // Connect to your Python Backend
      const response = await axios.post('http://127.0.0.1:8000/search', {
        query: query
      });
      setResults(response.data);
    } catch (err) {
      console.error(err);
      setError("Failed to fetch results. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header className="hero">
        <h1>🔍 AI Employee Recommender</h1>
        <p>Describe the ideal candidate, and our AI will find the best match.</p>
        
        <div className="search-box">
          <textarea 
            placeholder="Ex: I need a senior python developer who knows cloud infrastructure..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            rows="3"
          />
          <button onClick={handleSearch} disabled={loading}>
            {loading ? 'Searching...' : 'Find Matches'}
          </button>
        </div>
      </header>

      {error && <p className="error">{error}</p>}

      <div className="results-grid">
        {results.map((employee) => (
          <div key={employee.id} className="card">
            <div className="card-header">
              <h2>{employee.name}</h2>
              <span className={`score ${employee.similarity_score > 0.5 ? 'high' : 'low'}`}>
                {(employee.similarity_score * 100).toFixed(0)}% Match
              </span>
            </div>
            <h3>{employee.role}</h3>
            <p className="exp">{employee.experience} Years Experience</p>
            <p className="bio">"{employee.bio_snippet}"</p>
          </div>
        ))}
      </div>
      <footer className="footer">
        <p>
          Designed & Developed by <a href="https://www.linkedin.com/in/harsh-modi-85b32523b/" target="_blank" rel="noopener noreferrer">Harsh Modi</a>
        </p>
      </footer>
    </div>
  )
}

export default App