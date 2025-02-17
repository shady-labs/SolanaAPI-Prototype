from fastapi import FastAPI
from app.routes import nfts

app = FastAPI()

# Include routers for different functionalities
app.include_router(nfts.router, prefix="/nfts", tags=["NFTs"])
