from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
from solana.rpc.types import TokenAccountOpts
from config import RPC_URL, TOKEN_PROGRAM_ID

async def get_token_accounts(wallet_address: str):
    client = AsyncClient(RPC_URL)
    public_key = Pubkey.from_string(wallet_address)
    opts = TokenAccountOpts(
        program_id=Pubkey.from_string(TOKEN_PROGRAM_ID)
    )
    response = await client.get_token_accounts_by_owner(public_key, opts)
    await client.close()
    if response.value:
        return response.value
    else:
        return {"error": "No token accounts found"}