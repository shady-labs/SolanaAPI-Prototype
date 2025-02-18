from app.nfts.solana_rpc.accounts import get_token_accounts
from app.nfts.solana_rpc.nft import get_nft_data
from app.nfts.solana_rpc.proof import get_nft_proof

async def is_nft(asset):
    if not isinstance(asset, dict):
        return False
    account_data = asset.get("account", {}).get("data", {})
    if not isinstance(account_data, dict):
        return False
    parsed_info = account_data.get("parsed", {}).get("info", {})
    token_standard = parsed_info.get("tokenStandard")
    return token_standard in ["NonFungible", "ProgrammableNFT"]

async def get_all_nfts(wallet_address: str):
    tokens = await get_token_accounts(wallet_address)
    if not isinstance(tokens, list):
        return {"error": "Invalid token accounts response"}
    return [token for token in tokens if await is_nft(token)]

async def get_asset(mint_address: str):
    return {"mint_address": mint_address, "asset": await get_nft_data(mint_address)}

async def get_asset_proof(mint_address: str):
    return await get_nft_proof(mint_address)

async def get_assets_by_owner_service(wallet_address: str):
    return await get_token_accounts(wallet_address)

async def get_assets_by_collection_service(collection_address: str):
    return await get_token_accounts(collection_address)

async def get_assets_by_group_service(group_key: str, group_value: str):
    token_accounts = await get_token_accounts(group_value)
    return [token for token in token_accounts if group_key in token]