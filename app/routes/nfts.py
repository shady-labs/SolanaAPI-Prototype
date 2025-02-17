from fastapi import APIRouter
from app.services.nfts_service import get_all_nfts, get_nft_metadata, get_nfts_by_collection

router = APIRouter()

@router.get("/getAllNFTs")
def get_nfts(wallet_address: str):
    return get_all_nfts(wallet_address)

@router.get("/getNFTMetadata")
def get_nft_metadata_api(mint_address: str):
    return get_nft_metadata(mint_address)

@router.get("/getNFTsByCollection")
def get_nfts_by_collection_api(wallet_address: str, collection_address: str):
    return get_nfts_by_collection(wallet_address, collection_address)
