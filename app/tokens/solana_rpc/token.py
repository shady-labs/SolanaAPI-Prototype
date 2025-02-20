from solders.pubkey import Pubkey
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.rpc.async_api import AsyncClient
from config import RPC_URL

async def get_token_data(mint_address: str):
    """Get token data from the blockchain."""
    client = AsyncClient(RPC_URL)
    try:
        public_key = Pubkey.from_string(mint_address)
        response = await client.get_account_info(public_key)
        
        if response.value is None:
            return {"error": "Token data not found"}

        account_data = {
            "lamports": response.value.lamports,
            "owner": str(response.value.owner),
            "executable": response.value.executable,
            "rent_epoch": response.value.rent_epoch,
            "data": response.value.data
        }

        return account_data
    except Exception as e:
        return {"error": f"Failed to get token data: {str(e)}"}
    finally:
        await client.close()

async def get_token_metadata(mint_address: str):
    """Get token metadata."""
    try:
        TOKEN_METADATA_PROGRAM_ID = "metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s"
        
        mint_pubkey = Pubkey.from_string(mint_address)
        metadata_program_id = Pubkey.from_string(TOKEN_METADATA_PROGRAM_ID)

        # Compute Metadata PDA
        seeds = [
            bytearray("metadata".encode()),
            bytes(metadata_program_id),
            bytes(mint_pubkey)
        ]
        
        metadata_pda, _ = Pubkey.find_program_address(
            seeds,
            metadata_program_id
        )

        # Get metadata account info
        client = AsyncClient(RPC_URL)
        try:
            response = await client.get_account_info(metadata_pda)
            if not response.value:
                return {"error": "Token metadata not found"}

            # Parse metadata here
            # This would depend on your token metadata structure
            return {
                "address": str(metadata_pda),
                "data": response.value.data
            }
        finally:
            await client.close()

    except Exception as e:
        return {"error": f"Failed to get token metadata: {str(e)}"}

def get_token_program_id():
    """Get the SPL Token program ID."""
    return TOKEN_PROGRAM_ID

def get_associated_token_address(wallet: str, mint: str) -> str:
    """Get the associated token account address for a wallet and mint."""
    try:
        wallet_pubkey = Pubkey.from_string(wallet)
        mint_pubkey = Pubkey.from_string(mint)
        seeds = [
            bytes(wallet_pubkey),
            bytes(TOKEN_PROGRAM_ID),
            bytes(mint_pubkey)
        ]
        associated_token_address, _ = Pubkey.find_program_address(
            seeds,
            TOKEN_PROGRAM_ID
        )
        return str(associated_token_address)
    except Exception as e:
        return None

def is_token_account(account_info: dict) -> bool:
    """Check if an account is a token account."""
    try:
        return account_info.get("owner") == str(TOKEN_PROGRAM_ID)
    except:
        return False 