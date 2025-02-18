from solana.rpc.async_api import AsyncClient
from config import RPC_URL

class SolanaRPCClient:
    def __init__(self):
        self.client = AsyncClient(RPC_URL)

    async def get_account_info(self, account_address: str):
        try:
            response = await self.client.get_account_info(account_address)
            return response.value if response.value else {"error": "Account not found"}
        except Exception as e:
            return {"error": f"Failed to get account info: {str(e)}"}

    async def get_balance(self, account_address: str):
        try:
            response = await self.client.get_balance(account_address)
            return {"balance": response.value} if response.value else {"error": "Failed to get balance"}
        except Exception as e:
            return {"error": f"Failed to get balance: {str(e)}"}

    async def get_block(self, slot: int):
        try:
            response = await self.client.get_block(slot)
            return response.value if response.value else {"error": "Block not found"}
        except Exception as e:
            return {"error": f"Failed to get block: {str(e)}"}

    async def get_block_height(self):
        try:
            response = await self.client.get_block_height()
            return {"height": response.value} if response.value else {"error": "Failed to get block height"}
        except Exception as e:
            return {"error": f"Failed to get block height: {str(e)}"}

    async def get_latest_blockhash(self):
        try:
            response = await self.client.get_latest_blockhash()
            return response.value if response.value else {"error": "Failed to get latest blockhash"}
        except Exception as e:
            return {"error": f"Failed to get latest blockhash: {str(e)}"}

    async def get_slot(self):
        try:
            response = await self.client.get_slot()
            return {"slot": response.value} if response.value else {"error": "Failed to get slot"}
        except Exception as e:
            return {"error": f"Failed to get slot: {str(e)}"}

    async def get_block_commitment(self, block: int):
        try:
            response = await self.client.get_block_commitment(block)
            return response.value if response.value else {"error": "Block commitment not found"}
        except Exception as e:
            return {"error": f"Failed to get block commitment: {str(e)}"}

    async def get_block_production(self):
        try:
            response = await self.client.get_block_production()
            return response.value if response.value else {"error": "Block production data not found"}
        except Exception as e:
            return {"error": f"Failed to get block production: {str(e)}"}

    async def get_block_time(self, block: int):
        try:
            response = await self.client.get_block_time(block)
            return {"timestamp": response.value} if response.value else {"error": "Block time not found"}
        except Exception as e:
            return {"error": f"Failed to get block time: {str(e)}"}

    async def get_blocks(self, start_slot: int, end_slot: int = None):
        try:
            response = await self.client.get_blocks(start_slot, end_slot)
            return {"blocks": response.value} if response.value else {"error": "Blocks not found"}
        except Exception as e:
            return {"error": f"Failed to get blocks: {str(e)}"}

    async def get_cluster_nodes(self):
        try:
            response = await self.client.get_cluster_nodes()
            return {"nodes": response.value} if response.value else {"error": "Cluster nodes not found"}
        except Exception as e:
            return {"error": f"Failed to get cluster nodes: {str(e)}"}

    async def get_epoch_info(self):
        try:
            response = await self.client.get_epoch_info()
            return response.value if response.value else {"error": "Epoch info not found"}
        except Exception as e:
            return {"error": f"Failed to get epoch info: {str(e)}"}

    async def get_epoch_schedule(self):
        try:
            response = await self.client.get_epoch_schedule()
            return response.value if response.value else {"error": "Epoch schedule not found"}
        except Exception as e:
            return {"error": f"Failed to get epoch schedule: {str(e)}"}

    async def get_genesis_hash(self):
        try:
            response = await self.client.get_genesis_hash()
            return {"genesis_hash": response.value} if response.value else {"error": "Genesis hash not found"}
        except Exception as e:
            return {"error": f"Failed to get genesis hash: {str(e)}"}

    async def get_health(self):
        try:
            response = await self.client.get_health()
            return {"status": "ok"} if response.value else {"error": "Health check failed"}
        except Exception as e:
            return {"error": f"Failed to get health status: {str(e)}"}

    async def get_identity(self):
        try:
            response = await self.client.get_identity()
            return response.value if response.value else {"error": "Identity not found"}
        except Exception as e:
            return {"error": f"Failed to get identity: {str(e)}"}

    async def get_blocks_with_limit(self, start_slot: int, limit: int):
        try:
            response = await self.client.get_blocks_with_limit(start_slot, limit)
            return {"blocks": response.value} if response.value else {"error": "Blocks not found"}
        except Exception as e:
            return {"error": f"Failed to get blocks with limit: {str(e)}"}

    async def get_fee_for_message(self, message: str):
        try:
            response = await self.client.get_fee_for_message(message)
            return {"fee": response.value} if response.value else {"error": "Fee not found"}
        except Exception as e:
            return {"error": f"Failed to get fee for message: {str(e)}"}

    async def get_first_available_block(self):
        try:
            response = await self.client.get_first_available_block()
            return {"block": response.value} if response.value else {"error": "First available block not found"}
        except Exception as e:
            return {"error": f"Failed to get first available block: {str(e)}"}

    async def get_highest_snapshot_slot(self):
        try:
            response = await self.client.get_highest_snapshot_slot()
            return {"slot": response.value} if response.value else {"error": "Highest snapshot slot not found"}
        except Exception as e:
            return {"error": f"Failed to get highest snapshot slot: {str(e)}"}

    async def get_inflation_governor(self):
        try:
            response = await self.client.get_inflation_governor()
            return response.value if response.value else {"error": "Inflation governor not found"}
        except Exception as e:
            return {"error": f"Failed to get inflation governor: {str(e)}"}

    async def get_inflation_rate(self):
        try:
            response = await self.client.get_inflation_rate()
            return response.value if response.value else {"error": "Inflation rate not found"}
        except Exception as e:
            return {"error": f"Failed to get inflation rate: {str(e)}"}

    async def get_inflation_reward(self, addresses: list, epoch: int = None):
        try:
            response = await self.client.get_inflation_reward(addresses, epoch)
            return response.value if response.value else {"error": "Inflation reward not found"}
        except Exception as e:
            return {"error": f"Failed to get inflation reward: {str(e)}"}

    async def get_largest_accounts(self, filter_opt: str = None):
        try:
            response = await self.client.get_largest_accounts(filter_opt)
            return response.value if response.value else {"error": "Largest accounts not found"}
        except Exception as e:
            return {"error": f"Failed to get largest accounts: {str(e)}"}

    async def get_leader_schedule(self, slot: int = None):
        try:
            response = await self.client.get_leader_schedule(slot)
            return response.value if response.value else {"error": "Leader schedule not found"}
        except Exception as e:
            return {"error": f"Failed to get leader schedule: {str(e)}"}

    async def get_max_retransmit_slot(self):
        try:
            response = await self.client.get_max_retransmit_slot()
            return {"slot": response.value} if response.value else {"error": "Max retransmit slot not found"}
        except Exception as e:
            return {"error": f"Failed to get max retransmit slot: {str(e)}"}

    async def get_max_shred_insert_slot(self):
        try:
            response = await self.client.get_max_shred_insert_slot()
            return {"slot": response.value} if response.value else {"error": "Max shred insert slot not found"}
        except Exception as e:
            return {"error": f"Failed to get max shred insert slot: {str(e)}"}

    async def get_minimum_balance_for_rent_exemption(self, data_size: int):
        try:
            response = await self.client.get_minimum_balance_for_rent_exemption(data_size)
            return {"lamports": response.value} if response.value else {"error": "Minimum balance not found"}
        except Exception as e:
            return {"error": f"Failed to get minimum balance: {str(e)}"}

    async def get_multiple_accounts(self, pubkeys: list):
        try:
            response = await self.client.get_multiple_accounts(pubkeys)
            return response.value if response.value else {"error": "Accounts not found"}
        except Exception as e:
            return {"error": f"Failed to get multiple accounts: {str(e)}"}

    async def get_program_accounts(self, program_id: str, encoding: str = "base64"):
        try:
            response = await self.client.get_program_accounts(program_id, encoding=encoding)
            return response.value if response.value else {"error": "Program accounts not found"}
        except Exception as e:
            return {"error": f"Failed to get program accounts: {str(e)}"}

    async def get_recent_performance_samples(self):
        try:
            response = await self.client.get_recent_performance_samples()
            return response.value if response.value else {"error": "Performance samples not found"}
        except Exception as e:
            return {"error": f"Failed to get performance samples: {str(e)}"}

    async def get_recent_prioritization_fees(self, addresses: list = None):
        try:
            response = await self.client.get_recent_prioritization_fees(addresses)
            return response.value if response.value else {"error": "Prioritization fees not found"}
        except Exception as e:
            return {"error": f"Failed to get prioritization fees: {str(e)}"}

    async def get_signature_statuses(self, signatures: list, search_transaction_history: bool = False):
        try:
            response = await self.client.get_signature_statuses(signatures, search_transaction_history)
            return response.value if response.value else {"error": "Signature statuses not found"}
        except Exception as e:
            return {"error": f"Failed to get signature statuses: {str(e)}"}

    async def get_signatures_for_address(self, address: str, before: str = None, until: str = None, limit: int = None):
        try:
            response = await self.client.get_signatures_for_address(address, before, until, limit)
            return response.value if response.value else {"error": "Signatures not found"}
        except Exception as e:
            return {"error": f"Failed to get signatures for address: {str(e)}"}

    async def get_slot_leader(self):
        try:
            response = await self.client.get_slot_leader()
            return {"leader": response.value} if response.value else {"error": "Slot leader not found"}
        except Exception as e:
            return {"error": f"Failed to get slot leader: {str(e)}"}

    async def get_slot_leaders(self, start_slot: int, limit: int):
        try:
            response = await self.client.get_slot_leaders(start_slot, limit)
            return {"leaders": response.value} if response.value else {"error": "Slot leaders not found"}
        except Exception as e:
            return {"error": f"Failed to get slot leaders: {str(e)}"}

    async def get_stake_minimum_delegation(self):
        try:
            response = await self.client.get_stake_minimum_delegation()
            return {"lamports": response.value} if response.value else {"error": "Stake minimum delegation not found"}
        except Exception as e:
            return {"error": f"Failed to get stake minimum delegation: {str(e)}"}

    async def get_supply(self, commitment: str = None):
        try:
            response = await self.client.get_supply(commitment)
            return response.value if response.value else {"error": "Supply not found"}
        except Exception as e:
            return {"error": f"Failed to get supply: {str(e)}"}

    async def get_transaction(self, signature: str, encoding: str = "json"):
        try:
            response = await self.client.get_transaction(signature, encoding=encoding)
            return response.value if response.value else {"error": "Transaction not found"}
        except Exception as e:
            return {"error": f"Failed to get transaction: {str(e)}"}

    async def get_transaction_count(self, commitment: str = None):
        try:
            response = await self.client.get_transaction_count(commitment)
            return {"count": response.value} if response.value else {"error": "Transaction count not found"}
        except Exception as e:
            return {"error": f"Failed to get transaction count: {str(e)}"}

    async def get_recent_blockhash(self):
        try:
            response = await self.client.get_recent_blockhash()
            return response.value if response.value else {"error": "Recent blockhash not found"}
        except Exception as e:
            return {"error": f"Failed to get recent blockhash: {str(e)}"}

    async def send_transaction(self, transaction: str, recent_blockhash: str = None):
        try:
            response = await self.client.send_transaction(transaction, recent_blockhash)
            return {"signature": response.value} if response.value else {"error": "Failed to send transaction"}
        except Exception as e:
            return {"error": f"Failed to send transaction: {str(e)}"}

    async def simulate_transaction(self, transaction: str, sig_verify: bool = False):
        try:
            response = await self.client.simulate_transaction(transaction, sig_verify)
            return response.value if response.value else {"error": "Failed to simulate transaction"}
        except Exception as e:
            return {"error": f"Failed to simulate transaction: {str(e)}"}

    async def get_version(self):
        try:
            response = await self.client.get_version()
            return response.value if response.value else {"error": "Version info not found"}
        except Exception as e:
            return {"error": f"Failed to get version: {str(e)}"}

    async def get_vote_accounts(self):
        try:
            response = await self.client.get_vote_accounts()
            return response.value if response.value else {"error": "Vote accounts not found"}
        except Exception as e:
            return {"error": f"Failed to get vote accounts: {str(e)}"}

    # Add more methods as needed...

    async def close(self):
        await self.client.close() 