import base64
import json
from app.nfts.solana_rpc.nft import get_nft_data

async def get_nft_proof(mint_address: str):
    nft_data = await get_nft_data(mint_address)
    if nft_data and "data" in nft_data:
        proof = base64.b64encode(json.dumps(nft_data).encode()).decode()
        return {"mint_address": mint_address, "proof": proof}
    return {"error": "NFT proof not found"}