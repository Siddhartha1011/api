# Transaction Ranking System — Frontend
A modern React-based frontend for a transaction tracking, scoring, and ranking system.
This UI connects to a FastAPI + PostgreSQL backend and demonstrates real-time transaction processing, user summaries, and leaderboard ranking.

# Features
* 💸 Add new transactions
* 👤 View user summary (total amount, transaction count, score)
* 🏆 Live ranking leaderboard
* ⚡ Real-time API integration with backend


# API Endpoints Used
## Create Transaction 
POST /transaction

## Get User Summary
GET /summary/:userId

## Get Leaderboard
GET /ranking
