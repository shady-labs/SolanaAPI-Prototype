from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
from solana.rpc.types import TokenAccountOpts  # ✅ Correct import

RPC_URL = "https://api.mainnet-beta.solana.com"

async def get_token_accounts(wallet_address: str):
    client = AsyncClient(RPC_URL)
    public_key = Pubkey.from_string(wallet_address)

    opts = TokenAccountOpts(
        program_id=Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")  # ✅ Correct format
    )

    response = await client.get_token_accounts_by_owner(public_key, opts)
    await client.close()

    if response.value:  # ✅ Correctly accessing response
        return response.value
    else:
        return {"error": "No token accounts found"}
