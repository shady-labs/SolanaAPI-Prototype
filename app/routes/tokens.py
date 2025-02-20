from fastapi import APIRouter
from app.models.token import TokenAccountBalance, TokenAccount, TokenSupply
from app.tokens.solana_rpc.rpc_services import (
    get_token_account_balance_service,
    get_token_accounts_by_owner_service,
    get_token_supply_service,
    get_token_largest_accounts_service,
    get_token_accounts_by_delegate_service
)

# Create separate routers for GET and POST requests
get_router = APIRouter()
post_router = APIRouter()

@get_router.get("/getTokenAccountBalance", response_model=TokenAccountBalance)
async def get_token_account_balance(account: str):
    """Get token account balance."""
    return await get_token_account_balance_service(account)

@get_router.get("/getTokenAccountsByOwner", response_model=list[TokenAccount])
async def get_token_accounts_by_owner(owner: str, program_id: str = None):
    """Get all token accounts owned by the given account."""
    return await get_token_accounts_by_owner_service(owner, program_id)

@get_router.get("/getTokenSupply", response_model=TokenSupply)
async def get_token_supply(mint: str):
    """Get token supply."""
    return await get_token_supply_service(mint)

@get_router.get("/getTokenLargestAccounts")
async def get_token_largest_accounts(mint: str):
    """Get largest token accounts."""
    return await get_token_largest_accounts_service(mint)

@get_router.get("/getTokenAccountsByDelegate")
async def get_token_accounts_by_delegate(
    delegate: str, 
    program_id: str = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
):
    """Get all token accounts for a delegate."""
    try:
        return await get_token_accounts_by_delegate_service(delegate, program_id)
    except Exception as e:
        return {"error": str(e)}
