from fastapi import FastAPI
from app.routes.nfts import router as nft_router
from app.routes.tokens import router as token_router  # ✅ New Token API Route

app = FastAPI()

# Include NFT and Token routes
app.include_router(nft_router, prefix="/nfts")
app.include_router(token_router, prefix="/tokens")  # ✅ Token API Placeholder
