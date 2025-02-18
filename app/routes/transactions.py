from fastapi import APIRouter
from app.nfts.solana_rpc.rpc_services import (
    send_transaction_service,
    simulate_transaction_service
)

router = APIRouter()

@router.post("/sendTransaction")
async def send_transaction_api(transaction: str, recent_blockhash: str = None):
    """Send a transaction."""
    try:
        return await send_transaction_service(transaction, recent_blockhash)
    except Exception as e:
        return {"error": str(e)}

@router.post("/simulateTransaction")
async def simulate_transaction_api(transaction: str, sig_verify: bool = False):
    """Simulate a transaction."""
    try:
        return await simulate_transaction_service(transaction, sig_verify)
    except Exception as e:
        return {"error": str(e)} 