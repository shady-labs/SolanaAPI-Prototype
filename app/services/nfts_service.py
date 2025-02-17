import asyncio
from app.solana_rpc import get_token_accounts, get_metadata_from_mint

def get_all_nfts(wallet_address: str):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    token_accounts = loop.run_until_complete(get_token_accounts(wallet_address))
    
    # Filtering NFTs (metadata accounts, decimals = 0, etc.)
    nfts = [token for token in token_accounts if "account" in token]
    return {"wallet": wallet_address, "nfts": nfts}

def get_nft_metadata(mint_address: str):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    metadata = loop.run_until_complete(get_metadata_from_mint(mint_address))
    return {"mint_address": mint_address, "metadata": metadata}

def get_nfts_by_collection(wallet_address: str, collection_address: str):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    token_accounts = loop.run_until_complete(get_token_accounts(wallet_address))

    # Filtering NFTs that belong to a specific collection
    nfts = [
        token for token in token_accounts
        if "account" in token and token.get("collection", "") == collection_address
    ]
    
    return {"wallet": wallet_address, "collection": collection_address, "nfts": nfts}
