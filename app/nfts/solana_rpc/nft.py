from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
import base64
from config import RPC_URL

async def get_nft_data(mint_address: str):
    client = AsyncClient(RPC_URL)
    public_key = Pubkey.from_string(mint_address)
    response = await client.get_account_info(public_key)
    await client.close()

    if response.value is None:
        return {"error": "NFT data not found"}

    account_data = {
        "lamports": response.value.lamports,
        "owner": str(response.value.owner),
        "executable": response.value.executable,
        "rent_epoch": response.value.rent_epoch,
        "data": base64.b64encode(response.value.data).decode("utf-8") if response.value.data else None
    }

    return account_data
