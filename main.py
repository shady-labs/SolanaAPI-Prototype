from fastapi import FastAPI
from app.routes.nfts import router as nft_router

app = FastAPI()
app.include_router(nft_router, prefix="/nfts")