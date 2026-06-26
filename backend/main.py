from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from schemas import TransactionRequest
from models import User, Transaction
from crud import create_transaction

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:5173"  
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# GET /
# -----------------------------
from database import engine

@app.get("/")
def root():
    try:
        with engine.connect() as conn:
            return {"message": "Database connected successfully!"}
    except Exception as e:
        return {"error": str(e)}

# -----------------------------
# POST /transaction
# -----------------------------
@app.post("/transaction")
def transaction(req: TransactionRequest, db: Session = Depends(get_db)):
    return create_transaction(
        db,
        req.transactionId,
        req.userId,
        req.amount
    )


# -----------------------------
# GET /summary/:userId
# -----------------------------
@app.get("/summary/{user_id}")
def get_summary(user_id: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        return {"error": "User not found"}

    return {
        "userId": user.user_id,
        "totalTransactions": user.transaction_count,
        "totalAmount": float(user.total_amount),
        "score": float(user.score)
    }


# -----------------------------
# GET /ranking
# -----------------------------
@app.get("/ranking")
def get_ranking(db: Session = Depends(get_db)):

    users = db.query(User).order_by(User.score.desc()).limit(100).all()

    return [
        {
            "userId": u.user_id,
            "score": float(u.score),
            "totalAmount": float(u.total_amount),
            "transactions": u.transaction_count
        }
        for u in users
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)