# CryptoAnalyst AI - Cryptocurrency Analysis API

An AI-powered FastAPI application that provides intelligent cryptocurrency market analysis using real-time data from CoinGecko and LLM-powered insights.

## Features

- **Real-time Crypto Data**: Fetches live market data from CoinGecko API
- **AI-Powered Analysis**: Uses Llama 3.3 70B model via OpenRouter for intelligent market analysis
- **Structured Responses**: Returns well-formatted analysis with key factors and insights
- **RESTful API**: Simple POST endpoint for cryptocurrency analysis

## Prerequisites

- Python 3.8+
- OpenRouter API key
- Internet connection for CoinGecko API access

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <project-directory>
```

2. Install required dependencies:
```bash
pip install fastapi uvicorn requests langchain-core langchain-openai python-dotenv
```

3. Create a `.env` file in the project root:
```env
OPENROUTER_KEY=your_openrouter_api_key_here
OPENROUTER_URL=https://openrouter.ai/api/v1
COINGECKO_URL=https://api.coingecko.com/api/v3/coins/markets
```

4. Create a `models.py` file with the required Pydantic models:
```python
from pydantic import BaseModel
from typing import List

class CryptoRequest(BaseModel):
    coins: List[str]

class CryptoAnalysisResponse(BaseModel):
    # Define your response structure here
    pass
```

## Usage

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Access the interactive API documentation at `http://localhost:8000/docs`

### API Endpoint

**POST** `/crypto/analysis`

**Request Body:**
```json
{
  "coins": ["bitcoin", "ethereum", "cardano"]
}
```

**Response:**
Returns structured analysis for each cryptocurrency including:
- 3 key factors
- 3 market insights
- Analysis based on current metrics (price, market cap, volume, 24h change)

## Example Request

```bash
curl -X POST "http://localhost:8000/crypto/analysis" \
  -H "Content-Type: application/json" \
  -d '{
    "coins": ["bitcoin", "ethereum"]
  }'
```

## Project Structure

```
.
├── main.py                 # Main FastAPI application
├── models.py              # Pydantic models for request/response
├── .env                   # Environment variables (not in git)
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENROUTER_KEY` | Your OpenRouter API key for LLM access |
| `OPENROUTER_URL` | OpenRouter API base URL |
| `COINGECKO_URL` | CoinGecko API endpoint for market data |

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **LangChain**: Framework for LLM application development
- **OpenAI SDK**: For LLM integration via OpenRouter
- **Requests**: HTTP library for API calls
- **Python-dotenv**: Environment variable management

## How It Works

1. Client sends a POST request with a list of cryptocurrency IDs
2. Application fetches real-time market data from CoinGecko API
3. Market data is formatted and sent to Llama 3.3 70B model via OpenRouter
4. AI analyzes the data and generates structured insights
5. API returns formatted analysis with key factors and insights

## Error Handling

- Returns `400 Bad Request` if no coins are provided
- Validates cryptocurrency IDs against CoinGecko's supported coins
- Handles API connection errors gracefully

## Notes

- Use valid CoinGecko cryptocurrency IDs (e.g., "bitcoin", "ethereum", "cardano")
- The free tier of OpenRouter may have rate limits
- CoinGecko's free API has rate limits (check their documentation)

## License

[Specify your license here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

