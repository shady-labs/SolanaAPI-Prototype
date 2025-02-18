from fastapi import FastAPI
from app.routes.nfts import get_router as nft_get_router
from app.routes.nfts import post_router as nft_post_router
from app.routes.tokens import router as token_router

app = FastAPI()

# GET endpoints
app.include_router(nft_get_router, prefix="/nfts")
app.include_router(token_router, prefix="/tokens")

# POST endpoints
app.include_router(nft_post_router, prefix="/nfts")
