from fastapi import APIRouter
from app.nfts.das.services.nfts_service import (
    get_all_nfts, get_asset, get_asset_proof,
    get_assets_by_owner_service, get_assets_by_collection_service, get_assets_by_group_service
)

router = APIRouter()

@router.get("/getAllNFTs")
def get_nfts(wallet_address: str):
    return get_all_nfts(wallet_address)

@router.get("/getAsset")
def get_asset_api(mint_address: str):
    return get_asset(mint_address)

@router.get("/getAssetProof")
def get_asset_proof_api(mint_address: str):
    return get_asset_proof(mint_address)

@router.get("/getAssetsByOwner")
def get_assets_by_owner_api(wallet_address: str):
    return get_assets_by_owner_service(wallet_address)

@router.get("/getAssetsByCollection")
def get_assets_by_collection_api(collection_address: str):
    return get_assets_by_collection_service(collection_address)

@router.get("/getAssetsByGroup")
def get_assets_by_group_api(group_key: str, group_value: str):
    return get_assets_by_group_service(group_key, group_value)
