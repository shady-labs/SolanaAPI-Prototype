from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

RPC_URL = "https://api.mainnet-beta.solana.com" 

async def get_token_accounts(wallet_address: str):
    client = AsyncClient(RPC_URL)
    response = await client.get_token_accounts_by_owner(
        Pubkey(wallet_address),
        program_id=Pubkey("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"),
    )
    await client.close()
    return response["result"]["value"]

async def get_metadata_from_mint(mint_address: str):
    client = AsyncClient(RPC_URL)
    response = await client.get_account_info(Pubkey(mint_address))
    await client.close()
    return response["result"]["value"]


