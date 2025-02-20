from fastapi import HTTPException
from ..solana_rpc.token import get_token_data, get_token_metadata
from ..solana_rpc.rpc_client import TokenRPCClient

async def get_all_tokens(wallet_address: str):
    """Get all tokens for a wallet address."""
    client = TokenRPCClient()
    try:
        response = await client.get_token_accounts_by_owner(
            wallet_address,
            "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"  # SPL Token program
        )
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_token(mint_address: str):
    """Get token data and metadata."""
    try:
        # Get token data
        token_data = await get_token_data(mint_address)
        if "error" in token_data:
            raise HTTPException(status_code=400, detail=token_data["error"])

        # Get token metadata
        metadata = await get_token_metadata(mint_address)
        if "error" in metadata:
            raise HTTPException(status_code=400, detail=metadata["error"])

        return {
            "token": token_data,
            "metadata": metadata
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def get_token_balance(wallet_address: str, mint_address: str):
    """Get token balance for a specific token."""
    client = TokenRPCClient()
    try:
        response = await client.get_token_account_balance(wallet_address)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_tokens_by_owner_service(wallet_address: str):
    """Get all tokens owned by an address."""
    client = TokenRPCClient()
    try:
        response = await client.get_token_accounts_by_owner(wallet_address)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_token_supply_info(mint_address: str):
    """Get token supply information."""
    client = TokenRPCClient()
    try:
        response = await client.get_token_supply(mint_address)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close() 