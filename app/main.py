from fastapi import FastAPI
try:
    # Use full import paths
    from app.routes.nfts import get_router as nft_get_router, post_router as nft_post_router
    from app.routes.tokens import get_router as token_get_router, post_router as token_post_router
except Exception as e:
    print(f"Import error: {str(e)}")
    raise

app = FastAPI()

# GET endpoints
app.include_router(nft_get_router, prefix="/nfts")
app.include_router(token_get_router, prefix="/tokens")

# POST endpoints
app.include_router(nft_post_router, prefix="/nfts")
app.include_router(token_post_router, prefix="/tokens") 