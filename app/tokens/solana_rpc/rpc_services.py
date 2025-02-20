from fastapi import HTTPException
from .rpc_client import TokenRPCClient
from .token import get_token_data, get_token_metadata

async def get_token_account_balance_service(account: str):
    client = TokenRPCClient()
    try:
        response = await client.get_token_account_balance(account)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_token_accounts_by_owner_service(owner: str, program_id: str = None):
    client = TokenRPCClient()
    try:
        response = await client.get_token_accounts_by_owner(owner, program_id)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_token_supply_service(mint: str):
    client = TokenRPCClient()
    try:
        response = await client.get_token_supply(mint)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_token_largest_accounts_service(mint: str):
    client = TokenRPCClient()
    try:
        response = await client.get_token_largest_accounts(mint)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_token_accounts_by_delegate_service(delegate: str, program_id: str = None):
    client = TokenRPCClient()
    try:
        response = await client.get_token_accounts_by_delegate(delegate, program_id)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close() 