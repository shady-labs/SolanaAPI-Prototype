from pydantic import BaseModel, Field
from typing import List, Optional

class BalanceResponse(BaseModel):
    balance: int = Field(..., description="Account balance in lamports")

class BlockResponse(BaseModel):
    blockhash: str = Field(..., description="Block hash")
    previous_blockhash: str = Field(..., description="Previous block hash")
    parent_slot: int = Field(..., description="Parent slot number")
    transactions: List[dict] = Field(default=[], description="List of transactions")

class SignatureResponse(BaseModel):
    signature: str = Field(..., description="Transaction signature")
    slot: int = Field(..., description="Slot number")
    err: Optional[dict] = Field(None, description="Error if any")
    memo: Optional[str] = Field(None, description="Memo if any")
    block_time: Optional[int] = Field(None, description="Block time") 