# Stock AI Backend API

FastAPI backend for the Stock AI Dashboard.

## Features

- Real-time stock data for AAPL, MSFT, TSLA
- AI-powered trading suggestions
- RESTful API endpoints

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.11
- **Dependencies**: yfinance, uvicorn

## API Endpoints

- `GET /api/stock-trends` - Get real-time stock data and AI suggestions

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Deployment

Deployed to Azure App Service at: `https://stock-ai-backend.azurewebsites.net`

## License

MIT License
