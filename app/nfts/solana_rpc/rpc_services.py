from fastapi import HTTPException
from .rpc_client import SolanaRPCClient

async def get_account_info_service(account_address: str):
    client = SolanaRPCClient()
    try:
        response = await client.get_account_info(account_address)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_balance_service(account_address: str):
    client = SolanaRPCClient()
    try:
        response = await client.get_balance(account_address)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_block_service(slot: int):
    client = SolanaRPCClient()
    try:
        response = await client.get_block(slot)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_block_commitment_service(block: int):
    client = SolanaRPCClient()
    try:
        response = await client.get_block_commitment(block)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_block_production_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_block_production()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_block_time_service(block: int):
    client = SolanaRPCClient()
    try:
        response = await client.get_block_time(block)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_blocks_service(start_slot: int, end_slot: int = None):
    client = SolanaRPCClient()
    try:
        response = await client.get_blocks(start_slot, end_slot)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_cluster_nodes_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_cluster_nodes()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_epoch_info_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_epoch_info()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_epoch_schedule_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_epoch_schedule()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_genesis_hash_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_genesis_hash()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_health_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_health()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_identity_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_identity()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_blocks_with_limit_service(start_slot: int, limit: int):
    client = SolanaRPCClient()
    try:
        response = await client.get_blocks_with_limit(start_slot, limit)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_fee_for_message_service(message: str):
    client = SolanaRPCClient()
    try:
        response = await client.get_fee_for_message(message)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_first_available_block_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_first_available_block()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_highest_snapshot_slot_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_highest_snapshot_slot()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_inflation_governor_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_inflation_governor()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_inflation_rate_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_inflation_rate()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_inflation_reward_service(addresses: list, epoch: int = None):
    client = SolanaRPCClient()
    try:
        response = await client.get_inflation_reward(addresses, epoch)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_largest_accounts_service(filter_opt: str = None):
    client = SolanaRPCClient()
    try:
        response = await client.get_largest_accounts(filter_opt)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_leader_schedule_service(slot: int = None):
    client = SolanaRPCClient()
    try:
        response = await client.get_leader_schedule(slot)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_max_retransmit_slot_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_max_retransmit_slot()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_max_shred_insert_slot_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_max_shred_insert_slot()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_minimum_balance_for_rent_exemption_service(data_size: int):
    client = SolanaRPCClient()
    try:
        response = await client.get_minimum_balance_for_rent_exemption(data_size)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_multiple_accounts_service(pubkeys: list):
    client = SolanaRPCClient()
    try:
        response = await client.get_multiple_accounts(pubkeys)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_program_accounts_service(program_id: str, encoding: str = "base64"):
    client = SolanaRPCClient()
    try:
        response = await client.get_program_accounts(program_id, encoding=encoding)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_recent_performance_samples_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_recent_performance_samples()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_recent_prioritization_fees_service(addresses: list = None):
    client = SolanaRPCClient()
    try:
        response = await client.get_recent_prioritization_fees(addresses)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_signature_statuses_service(signatures: list, search_transaction_history: bool = False):
    client = SolanaRPCClient()
    try:
        response = await client.get_signature_statuses(signatures, search_transaction_history)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_signatures_for_address_service(address: str, before: str = None, until: str = None, limit: int = None):
    client = SolanaRPCClient()
    try:
        response = await client.get_signatures_for_address(address, before, until, limit)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_slot_leader_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_slot_leader()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_slot_leaders_service(start_slot: int, limit: int):
    client = SolanaRPCClient()
    try:
        response = await client.get_slot_leaders(start_slot, limit)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_stake_minimum_delegation_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_stake_minimum_delegation()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_supply_service(commitment: str = None):
    client = SolanaRPCClient()
    try:
        response = await client.get_supply(commitment)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_transaction_service(signature: str, encoding: str = "json"):
    client = SolanaRPCClient()
    try:
        response = await client.get_transaction(signature, encoding)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_transaction_count_service(commitment: str = None):
    client = SolanaRPCClient()
    try:
        response = await client.get_transaction_count(commitment)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_recent_blockhash_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_recent_blockhash()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def send_transaction_service(transaction: str, recent_blockhash: str = None):
    client = SolanaRPCClient()
    try:
        response = await client.send_transaction(transaction, recent_blockhash)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def simulate_transaction_service(transaction: str, sig_verify: bool = False):
    client = SolanaRPCClient()
    try:
        response = await client.simulate_transaction(transaction, sig_verify)
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_version_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_version()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

async def get_vote_accounts_service():
    client = SolanaRPCClient()
    try:
        response = await client.get_vote_accounts()
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"])
        return response
    finally:
        await client.close()

# ... rest of the RPC service methods ... 