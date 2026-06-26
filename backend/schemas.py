from pydantic import BaseModel, Field, field_validator


class TransactionRequest(BaseModel):
    transactionId: str = Field(..., min_length=1)
    userId: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)

    @field_validator("transactionId", "userId")
    @classmethod
    def clean_strings(cls, value: str):
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty.")

        return value