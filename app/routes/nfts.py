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

router = APIRouter()
client = Client(RPC_URL)

@router.get("/getAllNFTs")
async def get_nfts(wallet_address: str):
    return await get_all_nfts(wallet_address)

@router.get("/getAsset")
async def get_asset_api(mint_address: str):
    return await get_asset(mint_address)

@router.get("/getAssetProof")
async def get_asset_proof_api(mint_address: str):
    return await get_asset_proof(mint_address)

@router.get("/getAssetsByOwner")
async def get_assets_by_owner_api(wallet_address: str):
    return await get_assets_by_owner_service(wallet_address)

@router.get("/getAssetsByCollection")
async def get_assets_by_collection_api(collection_address: str):
    return await get_assets_by_collection_service(collection_address)

@router.get("/getAssetsByGroup")
async def get_assets_by_group_api(group_key: str, group_value: str):
    return await get_assets_by_group_service(group_key, group_value)

@router.get("/{mint_address}/getNFTMetadata")
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