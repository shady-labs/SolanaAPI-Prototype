from pydantic import BaseModel, Field

class AccountInfoResponse(BaseModel):
    lamports: int = Field(..., description="Account balance in lamports")
    owner: str = Field(..., description="Account owner's public key")
    executable: bool = Field(..., description="Whether the account contains a program")
    rent_epoch: int = Field(..., description="Next epoch when rent is due") 