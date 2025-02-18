from fastapi import APIRouter

router = APIRouter()

@router.get("/getTokens")
async def get_tokens(wallet_address: str):
    return {"message": "Token API will be added soon!"}
