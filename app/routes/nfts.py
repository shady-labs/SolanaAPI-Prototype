from fastapi import APIRouter
from solders.pubkey import Pubkey
from solana.rpc.api import Client
from config import RPC_URL
from app.nfts.das.services.nft_services import (
    get_all_nfts, get_asset, get_asset_proof,
    get_assets_by_owner_service, get_assets_by_collection_service, 
    get_assets_by_group_service, get_nft_metadata
)
from app.nfts.solana_rpc.nft import fetch_off_chain_metadata
from app.nfts.solana_rpc.rpc_client import SolanaRPCClient
from app.nfts.solana_rpc.rpc_services import (
    get_account_info_service,
    get_balance_service,
    get_block_service,
    get_block_commitment_service,
    get_block_production_service,
    get_block_time_service,
    get_blocks_service,
    get_cluster_nodes_service,
    get_epoch_info_service,
    get_epoch_schedule_service,
    get_genesis_hash_service,
    get_health_service,
    get_identity_service,
    get_blocks_with_limit_service,
    get_fee_for_message_service,
    get_first_available_block_service,
    get_highest_snapshot_slot_service,
    get_inflation_governor_service,
    get_inflation_rate_service,
    get_inflation_reward_service,
    get_largest_accounts_service,
    get_leader_schedule_service,
    get_max_retransmit_slot_service,
    get_max_shred_insert_slot_service,
    get_minimum_balance_for_rent_exemption_service,
    get_multiple_accounts_service,
    get_program_accounts_service,
    get_recent_performance_samples_service,
    get_recent_prioritization_fees_service,
    get_signature_statuses_service,
    get_signatures_for_address_service,
    get_slot_leader_service,
    get_slot_leaders_service,
    get_stake_minimum_delegation_service,
    get_supply_service,
    get_transaction_service,
    get_transaction_count_service,
    get_recent_blockhash_service,
    send_transaction_service,
    simulate_transaction_service,
    get_version_service,
    get_vote_accounts_service,
)
from app.models.transaction import SendTransactionRequest, TransactionResponse, ErrorResponse

# Create separate routers for GET and POST requests
get_router = APIRouter()
post_router = APIRouter()

client = Client(RPC_URL)

@get_router.get("/getAllNFTs")
async def get_nfts(wallet_address: str):
    return await get_all_nfts(wallet_address)

@get_router.get("/getAsset")
async def get_asset_api(mint_address: str):
    return await get_asset(mint_address)

@get_router.get("/getAssetProof")
async def get_asset_proof_api(mint_address: str):
    return await get_asset_proof(mint_address)

@get_router.get("/getAssetsByOwner")
async def get_assets_by_owner_api(wallet_address: str):
    return await get_assets_by_owner_service(wallet_address)

@get_router.get("/getAssetsByCollection")
async def get_assets_by_collection_api(collection_address: str):
    return await get_assets_by_collection_service(collection_address)

@get_router.get("/getAssetsByGroup")
async def get_assets_by_group_api(group_key: str, group_value: str):
    return await get_assets_by_group_service(group_key, group_value)

@get_router.get("/{mint_address}/getNFTMetadata")
async def get_nft_metadata(mint_address: str):
    """Fetch NFT metadata from Solana and its off-chain URI."""
    try:
        TOKEN_METADATA_PROGRAM_ID = "metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s"
        
        mint_pubkey = Pubkey.from_string(mint_address)
        metadata_program_id = Pubkey.from_string(TOKEN_METADATA_PROGRAM_ID)

        # Compute Metadata PDA
        seeds = [
            bytearray([109, 101, 116, 97, 100, 97, 116, 97]),  # "metadata" in bytes
            bytes(metadata_program_id),
            bytes(mint_pubkey)
        ]
        
        metadata_pda, _ = Pubkey.find_program_address(
            seeds,
            metadata_program_id
        )

        # Fetch account info
        response = client.get_account_info(metadata_pda)
        if not response or not response.value or not response.value.data:
            return {"error": "Metadata account not found"}

        # Parse metadata
        metadata = await get_nft_metadata(response.value.data)
        if "error" in metadata:
            return metadata

        # Fetch full metadata from URI
        if "uri" in metadata:
            off_chain_data = fetch_off_chain_metadata(metadata["uri"])
            metadata["off_chain"] = off_chain_data
            return metadata
            
        return {"error": "Invalid metadata format"}

    except Exception as e:
        return {"error": f"Failed to fetch metadata: {str(e)}"}

@get_router.get("/getAccountInfo")
async def get_account_info_api(account_address: str):
    """Get account information for the specified account address."""
    try:
        return await get_account_info_service(account_address)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getBalance")
async def get_balance_api(account_address: str):
    """Get balance for the specified account address."""
    try:
        return await get_balance_service(account_address)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getBlock")
async def get_block_api(slot: int):
    """Get block information for the specified slot."""
    try:
        return await get_block_service(slot)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getBlockHeight")
async def get_block_height_api():
    """Get the current block height."""
    client = SolanaRPCClient()
    try:
        return await client.get_block_height()
    except Exception as e:
        return {"error": str(e)}
    finally:
        await client.close()

@get_router.get("/rpc/getLatestBlockhash")
async def get_latest_blockhash_api():
    """Get the latest blockhash."""
    client = SolanaRPCClient()
    try:
        return await client.get_latest_blockhash()
    except Exception as e:
        return {"error": str(e)}
    finally:
        await client.close()

@get_router.get("/rpc/getSlot")
async def get_slot_api():
    """Get the current slot."""
    client = SolanaRPCClient()
    try:
        return await client.get_slot()
    except Exception as e:
        return {"error": str(e)}
    finally:
        await client.close()

@get_router.get("/rpc/getBlockCommitment")
async def get_block_commitment_api(block: int):
    """Get block commitment for the specified block."""
    try:
        return await get_block_commitment_service(block)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getBlockProduction")
async def get_block_production_api():
    """Get block production information."""
    try:
        return await get_block_production_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getBlockTime")
async def get_block_time_api(block: int):
    """Get the estimated production time of a block."""
    try:
        return await get_block_time_service(block)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getBlocks")
async def get_blocks_api(start_slot: int, end_slot: int = None):
    """Get a list of confirmed blocks."""
    try:
        return await get_blocks_service(start_slot, end_slot)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getClusterNodes")
async def get_cluster_nodes_api():
    """Get information about all the nodes participating in the cluster."""
    try:
        return await get_cluster_nodes_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getEpochInfo")
async def get_epoch_info_api():
    """Get information about the current epoch."""
    try:
        return await get_epoch_info_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getEpochSchedule")
async def get_epoch_schedule_api():
    """Get epoch schedule information."""
    try:
        return await get_epoch_schedule_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getGenesisHash")
async def get_genesis_hash_api():
    """Get the genesis hash."""
    try:
        return await get_genesis_hash_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getHealth")
async def get_health_api():
    """Get the node's health."""
    try:
        return await get_health_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getIdentity")
async def get_identity_api():
    """Get the identity pubkey for the current node."""
    try:
        return await get_identity_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getBlocksWithLimit")
async def get_blocks_with_limit_api(start_slot: int, limit: int):
    """Get a list of confirmed blocks with limit."""
    try:
        return await get_blocks_with_limit_service(start_slot, limit)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getFeeForMessage")
async def get_fee_for_message_api(message: str):
    """Get the fee for a message."""
    try:
        return await get_fee_for_message_service(message)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getFirstAvailableBlock")
async def get_first_available_block_api():
    """Get the first available block."""
    try:
        return await get_first_available_block_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getHighestSnapshotSlot")
async def get_highest_snapshot_slot_api():
    """Get the highest snapshot slot."""
    try:
        return await get_highest_snapshot_slot_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getInflationGovernor")
async def get_inflation_governor_api():
    """Get the inflation governor parameters."""
    try:
        return await get_inflation_governor_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getInflationRate")
async def get_inflation_rate_api():
    """Get the inflation rate."""
    try:
        return await get_inflation_rate_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getInflationReward")
async def get_inflation_reward_api(addresses: list, epoch: int = None):
    """Get inflation reward for a list of addresses."""
    try:
        return await get_inflation_reward_service(addresses, epoch)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getLargestAccounts")
async def get_largest_accounts_api(filter_opt: str = None):
    """Get the largest accounts."""
    try:
        return await get_largest_accounts_service(filter_opt)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getLeaderSchedule")
async def get_leader_schedule_api(slot: int = None):
    """Get the leader schedule."""
    try:
        return await get_leader_schedule_service(slot)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getMaxRetransmitSlot")
async def get_max_retransmit_slot_api():
    """Get the maximum retransmit slot."""
    try:
        return await get_max_retransmit_slot_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getMaxShredInsertSlot")
async def get_max_shred_insert_slot_api():
    """Get the maximum shred insert slot."""
    try:
        return await get_max_shred_insert_slot_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getMinimumBalanceForRentExemption")
async def get_minimum_balance_for_rent_exemption_api(data_size: int):
    """Get the minimum balance for rent exemption."""
    try:
        return await get_minimum_balance_for_rent_exemption_service(data_size)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getMultipleAccounts")
async def get_multiple_accounts_api(pubkeys: list):
    """Get information about multiple accounts."""
    try:
        return await get_multiple_accounts_service(pubkeys)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getProgramAccounts")
async def get_program_accounts_api(program_id: str, encoding: str = "base64"):
    """Get all accounts owned by a program."""
    try:
        return await get_program_accounts_service(program_id, encoding)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getRecentPerformanceSamples")
async def get_recent_performance_samples_api():
    """Get recent performance samples."""
    try:
        return await get_recent_performance_samples_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getRecentPrioritizationFees")
async def get_recent_prioritization_fees_api(addresses: list = None):
    """Get recent prioritization fees."""
    try:
        return await get_recent_prioritization_fees_service(addresses)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getSignatureStatuses")
async def get_signature_statuses_api(signatures: list, search_transaction_history: bool = False):
    """Get the status of a list of signatures."""
    try:
        return await get_signature_statuses_service(signatures, search_transaction_history)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getSignaturesForAddress")
async def get_signatures_for_address_api(
    address: str, 
    before: str = None, 
    until: str = None, 
    limit: int = None
):
    """Get signatures for address."""
    try:
        return await get_signatures_for_address_service(address, before, until, limit)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getSlotLeader")
async def get_slot_leader_api():
    """Get the current slot leader."""
    try:
        return await get_slot_leader_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getSlotLeaders")
async def get_slot_leaders_api(start_slot: int, limit: int):
    """Get slot leaders for a slot range."""
    try:
        return await get_slot_leaders_service(start_slot, limit)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getStakeMinimumDelegation")
async def get_stake_minimum_delegation_api():
    """Get the stake minimum delegation."""
    try:
        return await get_stake_minimum_delegation_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getSupply")
async def get_supply_api(commitment: str = None):
    """Get information about the current supply."""
    try:
        return await get_supply_service(commitment)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getTransaction")
async def get_transaction_api(signature: str, encoding: str = "json"):
    """Get transaction details."""
    try:
        return await get_transaction_service(signature, encoding)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getTransactionCount")
async def get_transaction_count_api(commitment: str = None):
    """Get current transaction count."""
    try:
        return await get_transaction_count_service(commitment)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getRecentBlockhash")
async def get_recent_blockhash_api():
    """Get a recent blockhash."""
    try:
        return await get_recent_blockhash_service()
    except Exception as e:
        return {"error": str(e)}

@post_router.post("/sendTransaction", 
    response_model=TransactionResponse,
    responses={400: {"model": ErrorResponse}})
async def send_transaction_api(request: SendTransactionRequest):
    """Send a transaction."""
    try:
        response = await send_transaction_service(
            request.transaction, 
            request.recent_blockhash
        )
        return TransactionResponse(signature=response["signature"])
    except Exception as e:
        return ErrorResponse(error=str(e))

@post_router.post("/simulateTransaction")
async def simulate_transaction_api(transaction: str, sig_verify: bool = False):
    """Simulate a transaction."""
    try:
        return await simulate_transaction_service(transaction, sig_verify)
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getVersion")
async def get_version_api():
    """Get Solana version information."""
    try:
        return await get_version_service()
    except Exception as e:
        return {"error": str(e)}

@get_router.get("/rpc/getVoteAccounts")
async def get_vote_accounts_api():
    """Get all vote accounts."""
    try:
        return await get_vote_accounts_service()
    except Exception as e:
        return {"error": str(e)}