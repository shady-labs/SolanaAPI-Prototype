from pydantic import BaseModel, Field

class NFTMetadataResponse(BaseModel):
    name: str = Field(..., description="NFT name")
    symbol: str = Field(..., description="NFT symbol")
    uri: str = Field(..., description="Metadata URI")
    seller_fee_basis_points: int = Field(..., description="Seller fee basis points")
    creators: list | None = Field(None, description="List of creators")
    off_chain: dict | None = Field(None, description="Off-chain metadata") 