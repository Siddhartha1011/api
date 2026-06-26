from sqlalchemy.orm import Session
from models import User, Transaction
from sqlalchemy.exc import IntegrityError
from decimal import Decimal
import math

from rate_limiter import is_rate_limited


def get_or_create_user(db: Session, user_id: str):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        user = User(user_id=user_id)
        db.add(user)
        db.flush()   

    return user


def calculate_score(total_amount, transaction_count):
    return (
        0.4 * math.log(total_amount + 1)
        + 0.3 * math.sqrt(transaction_count)
        + 0.3 * transaction_count
    )


def create_transaction(db, tx_id: str, user_id: str, amount: float):

    if is_rate_limited(user_id):
        return {"error": "Rate limit exceeded"}

    amount = Decimal(str(amount))

    try:
        user = get_or_create_user(db, user_id)

        user = db.query(User)\
            .filter(User.id == user.id)\
            .with_for_update()\
            .first()

        if not user:
            return {"error": "User not found"}

        tx = Transaction(
            transaction_id=tx_id,
            user_pk=user.id,
            amount=amount
        )

        db.add(tx)

        user.total_amount = Decimal(user.total_amount or 0) + amount
        user.transaction_count += 1

        user.score = calculate_score(
            float(user.total_amount),
            user.transaction_count
        )

        db.commit()
        db.refresh(user)   

        return {"status": "success"}

    except IntegrityError:
        db.rollback()
        return {"error": "Duplicate transaction"}

    except Exception as e:
        db.rollback()   
        return {"error": str(e)}