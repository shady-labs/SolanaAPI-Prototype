import asyncio
from app.nfts.solana_rpc.accounts import get_token_accounts
from app.nfts.solana_rpc.nft import get_nft_data
from app.nfts.solana_rpc.proof import get_nft_proof

async def get_assets_by_owner(wallet_address: str):
    return await get_token_accounts(wallet_address)

async def get_assets_by_collection(collection_address: str):
    return await get_token_accounts(collection_address)

async def get_assets_by_group(group_key: str, group_value: str):
    token_accounts = await get_token_accounts(group_value)
    return [token for token in token_accounts if group_key in token]

def get_all_nfts(wallet_address: str):
    return asyncio.run(get_assets_by_owner(wallet_address))

def get_asset(mint_address: str):
    return {"mint_address": mint_address, "asset": asyncio.run(get_nft_data(mint_address))}

def get_asset_proof(mint_address: str):
    return asyncio.run(get_nft_proof(mint_address))

def get_assets_by_owner_service(wallet_address: str):
    return asyncio.run(get_assets_by_owner(wallet_address))

def get_assets_by_collection_service(collection_address: str):
    return asyncio.run(get_assets_by_collection(collection_address))

def get_assets_by_group_service(group_key: str, group_value: str):
    return asyncio.run(get_assets_by_group(group_key, group_value))