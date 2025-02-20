from solana.rpc.async_api import AsyncClient
from config import RPC_URL

class TokenRPCClient:
    def __init__(self):
        self.client = AsyncClient(RPC_URL)

    async def get_token_account_balance(self, account: str):
        try:
            response = await self.client.get_token_account_balance(account)
            return response.value if response.value else {"error": "Token account not found"}
        except Exception as e:
            return {"error": f"Failed to get token balance: {str(e)}"}

    async def get_token_accounts_by_owner(self, owner: str, program_id: str = None):
        try:
            response = await self.client.get_token_accounts_by_owner(owner, program_id)
            return response.value if response.value else {"error": "No token accounts found"}
        except Exception as e:
            return {"error": f"Failed to get token accounts: {str(e)}"}

    async def get_token_supply(self, mint: str):
        try:
            response = await self.client.get_token_supply(mint)
            return response.value if response.value else {"error": "Token supply not found"}
        except Exception as e:
            return {"error": f"Failed to get token supply: {str(e)}"}

    async def get_token_largest_accounts(self, mint: str):
        try:
            response = await self.client.get_token_largest_accounts(mint)
            return response.value if response.value else {"error": "Token accounts not found"}
        except Exception as e:
            return {"error": f"Failed to get largest accounts: {str(e)}"}

    async def get_token_accounts_by_delegate(self, delegate: str, program_id: str = None):
        try:
            response = await self.client.get_token_accounts_by_delegate(delegate, program_id)
            return response.value if response.value else {"error": "No token accounts found"}
        except Exception as e:
            return {"error": f"Failed to get token accounts: {str(e)}"}

    async def close(self):
        await self.client.close() 