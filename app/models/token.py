from pydantic import BaseModel, Field
from typing import Optional, List

class TokenAccountBalance(BaseModel):
    amount: str = Field(..., description="Token amount")
    decimals: int = Field(..., description="Token decimals")
    ui_amount: float = Field(..., description="Token amount in UI format")

class TokenAccount(BaseModel):
    mint: str = Field(..., description="Token mint address")
    owner: str = Field(..., description="Account owner's public key")
    amount: str = Field(..., description="Token amount")
    delegate: Optional[str] = Field(None, description="Delegate address if any")
    state: str = Field(..., description="Account state")
    is_native: bool = Field(..., description="Whether this is a native token")
    delegated_amount: str = Field(..., description="Delegated token amount")
    close_authority: Optional[str] = Field(None, description="Close authority if any")

class TokenSupply(BaseModel):
    amount: str = Field(..., description="Total supply amount")
    decimals: int = Field(..., description="Token decimals")
    ui_amount: float = Field(..., description="Total supply in UI format")

class TokenMintInfo(BaseModel):
    mint_authority: Optional[str] = Field(None, description="Mint authority address")
    supply: str = Field(..., description="Total token supply")
    decimals: int = Field(..., description="Token decimals")
    freeze_authority: Optional[str] = Field(None, description="Freeze authority address") 