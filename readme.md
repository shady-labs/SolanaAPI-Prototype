```markdown
# Solana NFT & Token API

A FastAPI service for interacting with Solana NFTs and Tokens, featuring both DAS (Digital Asset Standard) and RPC support.

## Project Structure

```bash
app/
├── nfts/
│   ├── das/
│   │   └── services/
│   │       └── nft_services.py    # DAS API implementation
│   └── solana_rpc/
│       ├── rpc_services.py        # NFT RPC services
│       └── rpc_client.py          # NFT RPC client
├── tokens/
│   └── solana_rpc/
│       ├── rpc_services.py        # Token RPC services
│       ├── rpc_client.py          # Token RPC client
│       └── token.py               # Token utilities
└── routes/
    ├── nfts.py                    # NFT endpoints
    └── tokens.py                  # Token endpoints
```

## Available Endpoints

### Token Endpoints
- `GET /tokens/getTokenAccountBalance`
- `GET /tokens/getTokenAccountsByOwner`
- `GET /tokens/getTokenSupply`
- `GET /tokens/getTokenLargestAccounts`
- `GET /tokens/getTokenAccountsByDelegate`

### NFT Endpoints (DAS)
- `GET /nfts/getAllNFTs`
- `GET /nfts/getAsset`
- `GET /nfts/getAssetProof`
- `GET /nfts/getAssetsByOwner`
- `GET /nfts/getAssetsByCollection`
- `GET /nfts/getAssetsByGroup`

### RPC Endpoints
- `GET /nfts/rpc/getAccountInfo`
- `GET /nfts/rpc/getBalance`
- `GET /nfts/rpc/getBlockHeight`
- `GET /nfts/rpc/getLatestBlockhash`
- `POST /nfts/sendTransaction`
- `POST /nfts/simulateTransaction`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure RPC endpoint in `config.py`:
```python
RPC_URL = "https://api.mainnet-beta.solana.com"  # or your preferred endpoint
```

4. Run the server:
```bash
uvicorn app.main:app --reload
```

## Testing
Run the test suite:
```bash
python tests/test_endpoints.py
```

## Requirements
- FastAPI
- Uvicorn
- Solana.py
- Solders
- SPL Token Client
- Pydantic
- Requests

See `requirements.txt` for complete list.
```
