import requests
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

BASE_URL = "http://127.0.0.1:8000"

# Set up logging
logging.basicConfig(
    filename=f'api_test_logs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class EndpointTester:
    def __init__(self):
        self.success_count = 0
        self.failure_count = 0
        
    def print_header(self, text: str):
        print(f"\n{Fore.CYAN}{'='*20} {text} {'='*20}{Style.RESET_ALL}")
        logging.info(f"\n=== {text} ===")

    def print_result(self, method: str, endpoint: str, status: int, success: bool):
        color = Fore.GREEN if success else Fore.RED
        status_text = "SUCCESS" if success else "FAILED"
        print(f"{color}{method:<7} {endpoint:<50} [{status:^5}] {status_text}{Style.RESET_ALL}")

    def test_endpoint(self, endpoint: str, method: str = "GET", params: Optional[Dict] = None, data: Optional[Dict] = None) -> Optional[requests.Response]:
        url = f"{BASE_URL}{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, params=params)
            else:  # POST
                response = requests.post(url, json=data)
            
            success = 200 <= response.status_code < 300
            self.print_result(method, endpoint, response.status_code, success)
            
            if success:
                self.success_count += 1
            else:
                self.failure_count += 1

            # Log details
            log_message = f"\n{method} {endpoint}"
            if params:
                log_message += f"\nParams: {params}"
            if data:
                log_message += f"\nData: {data}"
            log_message += f"\nStatus: {response.status_code}"
            
            if success:
                logging.info(f"SUCCESS - {log_message}")
            else:
                logging.error(f"FAILED - {log_message}\nResponse: {response.text}")
                print(f"{Fore.YELLOW}Response: {response.text}{Style.RESET_ALL}")

            return response
        except Exception as e:
            error_msg = f"Error testing {endpoint}: {str(e)}"
            logging.error(error_msg)
            print(f"{Fore.RED}{error_msg}{Style.RESET_ALL}")
            self.failure_count += 1
            return None

    def test_all_endpoints(self):
        self.print_header("NFT ENDPOINTS")
        self._test_nft_endpoints()

        self.print_header("TOKEN ENDPOINTS")
        self._test_token_endpoints()

        self.print_header("BASIC RPC ENDPOINTS")
        self._test_basic_rpc_endpoints()

        self.print_header("BLOCK-RELATED ENDPOINTS")
        self._test_block_endpoints()

        self.print_header("TRANSACTION ENDPOINTS")
        self._test_transaction_endpoints()

        self.print_header("SYSTEM INFO ENDPOINTS")
        self._test_system_endpoints()

        self._print_summary()

    def _test_nft_endpoints(self):
        nft_endpoints = [
            ("/nfts/getAllNFTs", {"wallet_address": "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg"}),
            ("/nfts/getAsset", {"mint_address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"}),
            ("/nfts/getAssetProof", {"mint_address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"}),
            ("/nfts/getAssetsByOwner", {"wallet_address": "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg"}),
            ("/nfts/getAssetsByCollection", {"collection_address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"}),
            ("/nfts/getAssetsByGroup", {"group_key": "collection", "group_value": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"})
        ]
        for endpoint, params in nft_endpoints:
            self.test_endpoint(endpoint, params=params)

    def _test_token_endpoints(self):
        self.print_header("TOKEN ENDPOINTS")
        
        # Known token addresses for testing
        token_mint = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"  # USDC
        token_account = "FbQdXCQgGQYj3xcGeryVVFjKCTsAuu53vmCRtmjQEqM5"
        owner_address = "83astBRguLMdt2h5U1Tpdq5tjFoJ6noeGwaY3mDLVcri"  # Sample from Helius docs
        
        token_endpoints = [
            # Basic token info endpoints
            ("/tokens/getTokenAccountBalance", {"account": token_account}),
            ("/tokens/getTokenAccountsByOwner", {
                "owner": owner_address,
                "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"  # SPL Token program ID
            }),
            ("/tokens/getTokenSupply", {"mint": token_mint}),
            ("/tokens/getTokenLargestAccounts", {"mint": token_mint}),
            # Additional token endpoints from Helius
            ("/tokens/getTokenAccountsByDelegate", {
                "delegate": owner_address,
                "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
            })
        ]

        for endpoint, params in token_endpoints:
            self.test_endpoint(endpoint, params=params)

        # Test with commitment parameter
        self.test_endpoint(
            "/tokens/getTokenAccountBalance", 
            params={
                "account": token_account,
                "commitment": "finalized"
            }
        )

    def _test_basic_rpc_endpoints(self):
        basic_endpoints = [
            ("/nfts/rpc/getAccountInfo", {"account_address": "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg"}),
            ("/nfts/rpc/getBalance", {"account_address": "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg"}),
            ("/nfts/rpc/getBlockHeight", None),
            ("/nfts/rpc/getLatestBlockhash", None),
            ("/nfts/rpc/getSlot", None)
        ]
        for endpoint, params in basic_endpoints:
            self.test_endpoint(endpoint, params=params)

    def _test_block_endpoints(self):
        slot_response = self.test_endpoint("/nfts/rpc/getSlot")
        if slot_response and slot_response.status_code == 200:
            current_slot = slot_response.json().get("slot")
            block_endpoints = [
                ("/nfts/rpc/getBlock", {"slot": current_slot}),
                ("/nfts/rpc/getBlockTime", {"block": current_slot}),
                ("/nfts/rpc/getBlockCommitment", {"block": current_slot}),
                ("/nfts/rpc/getBlocks", {"start_slot": current_slot - 10, "end_slot": current_slot}),
                ("/nfts/rpc/getBlocksWithLimit", {"start_slot": current_slot - 10, "limit": 5}),
                ("/nfts/rpc/getLeaderSchedule", {"slot": current_slot})
            ]
            for endpoint, params in block_endpoints:
                self.test_endpoint(endpoint, params=params)

    def _test_transaction_endpoints(self):
        # Test POST endpoints
        transaction_data = {
            "transaction": "base58_encoded_transaction",
            "recent_blockhash": "recent_blockhash_value"
        }
        self.test_endpoint("/nfts/sendTransaction", method="POST", data=transaction_data)
        self.test_endpoint("/nfts/simulateTransaction", method="POST", 
                          data={"transaction": "base58_encoded_transaction"})

    def _test_system_endpoints(self):
        system_endpoints = [
            ("/nfts/rpc/getBlockProduction", None),
            ("/nfts/rpc/getEpochInfo", None),
            ("/nfts/rpc/getEpochSchedule", None),
            ("/nfts/rpc/getGenesisHash", None),
            ("/nfts/rpc/getHealth", None),
            ("/nfts/rpc/getIdentity", None),
            ("/nfts/rpc/getInflationGovernor", None),
            ("/nfts/rpc/getInflationRate", None),
            ("/nfts/rpc/getVersion", None),
            ("/nfts/rpc/getVoteAccounts", None)
        ]
        for endpoint, params in system_endpoints:
            self.test_endpoint(endpoint, params=params)

    def _print_summary(self):
        total = self.success_count + self.failure_count
        success_rate = (self.success_count / total * 100) if total > 0 else 0
        
        self.print_header("TEST SUMMARY")
        print(f"{Fore.GREEN}Successful: {self.success_count}{Style.RESET_ALL}")
        print(f"{Fore.RED}Failed: {self.failure_count}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Success Rate: {success_rate:.1f}%{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}Starting API Tests...{Style.RESET_ALL}")
    tester = EndpointTester()
    tester.test_all_endpoints()
    print(f"\n{Fore.CYAN}Tests completed. Check the log file for detailed results.{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 