from pydantic import BaseModel, Field

# Request Models
class SendTransactionRequest(BaseModel):
    transaction: str = Field(..., description="Transaction data as base-58 encoded string")
    recent_blockhash: str | None = Field(None, description="Recent blockhash (optional)")

# Response Models
class TransactionResponse(BaseModel):
    signature: str = Field(..., description="Transaction signature")

class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message") 