import requests
import base64
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
from construct import Struct, Bytes, Int32ul
from config import RPC_URL

# Define Metaplex Metadata structure
METADATA_SCHEMA = Struct(
    "key" / Int32ul,  # First byte is key
    "update_authority" / Bytes(32),
    "mint" / Bytes(32),
    "data_size" / Int32ul,  # Size of the following data
    "name_len" / Int32ul,  # Length of name string
    "name" / Bytes(32),
    "symbol_len" / Int32ul,  # Length of symbol string
    "symbol" / Bytes(10),
    "uri_len" / Int32ul,  # Length of uri string
    "uri" / Bytes(200),
    "seller_fee_basis_points" / Int32ul,
    "creators_present" / Int32ul
)

async def get_nft_metadata(account_data):
    try:
        metadata = METADATA_SCHEMA.parse(account_data)
        
        # Clean up the bytes by removing null bytes and decode
        def clean_bytes(b, length):
            # Take only the specified length and remove all control characters
            cleaned = b[:length].decode('utf-8', errors='ignore')
            # Remove all control characters and extra whitespace
            cleaned = ''.join(c for c in cleaned if c.isprintable() and c != '\x00').strip()
            return cleaned

        # Get cleaned metadata fields using their lengths
        name = clean_bytes(metadata.name, metadata.name_len)
        symbol = clean_bytes(metadata.symbol, metadata.symbol_len)
        uri = clean_bytes(metadata.uri, metadata.uri_len)

        # Fix URI format
        if uri.startswith('/'):
            uri = f"https:{uri}"
        elif not uri.startswith('http'):
            uri = f"https://{uri}"

        # Ensure proper URL format
        uri = uri.replace('//', '/')  # Fix double slashes
        uri = uri.replace('https:/', 'https://')  # Fix protocol
        uri = uri.split('\x00')[0]  # Remove any remaining null bytes
        uri = uri.split('\x01')[0]  # Remove any control characters

        # Validate required fields
        if not uri:
            return {"error": "Missing or invalid URI in metadata"}

        return {
            "name": name or "Unknown",
            "symbol": symbol or "",
            "uri": uri,
            "update_authority": metadata.update_authority.hex(),
            "mint": metadata.mint.hex(),
            "seller_fee_basis_points": metadata.seller_fee_basis_points
        }
    except Exception as e:
        print(f"Raw data (first 100 bytes): {account_data[:100].hex()}")
        return {"error": f"Failed to parse metadata: {str(e)}"}

def fetch_off_chain_metadata(uri):
    """Fetch NFT metadata from off-chain storage (Arweave, IPFS)."""
    try:
        response = requests.get(uri, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Failed to fetch off-chain metadata: {str(e)}"}

async def get_nft_data(mint_address: str):
    client = AsyncClient(RPC_URL)  # Create client instance
    public_key = Pubkey.from_string(mint_address)
    response = await client.get_account_info(public_key)
    await client.close()

    if response.value is None:
        return {"error": "NFT data not found"}

    account_data = {
        "lamports": response.value.lamports,
        "owner": str(response.value.owner),
        "executable": response.value.executable,
        "rent_epoch": response.value.rent_epoch,
        "data": base64.b64encode(response.value.data).decode("utf-8") if response.value.data else None
    }

    return account_data