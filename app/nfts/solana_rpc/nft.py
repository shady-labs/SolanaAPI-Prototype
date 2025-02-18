from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

RPC_URL = "https://api.mainnet-beta.solana.com"

async def get_nft_data(mint_address: str):
    client = AsyncClient(RPC_URL)
    public_key = Pubkey.from_string(mint_address)
    response = await client.get_account_info(public_key)
    await client.close()
    return response["result"]["value"]