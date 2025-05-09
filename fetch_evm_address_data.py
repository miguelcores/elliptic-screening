import csv
import requests
import sys


API_KEY = "B1fnQQBlEBvYGlmA0CHD8BPDYTZRMsHv"


def fetch_eth_balance(address):
    """
    Fetch the token balances and metadata for a given address using the Dune API excluding spam tokens
        Below query is used to determine if something is spam
            https://dune.com/queries/3804603
        Additionally, any token with less than $100 of onchain liquidity is excluded
    """
    url = f"https://api.dune.com/api/echo/v1/balances/evm/{address}?exclude_spam_tokens"
    
    headers = {"X-Dune-Api-Key": API_KEY}

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "balances" in data:
            
            result = {
                "address": data.get("wallet_address", address),
                "token_count": len(data["balances"]),
                "tokens": []
            }
            
            for balance in data["balances"]:
                token_data = {
                    "chain": balance.get("chain"),
                    "chain_id": balance.get("chain_id", None),
                    "symbol": balance.get("symbol", None),
                    "name": balance.get("name", None),
                    "address": balance.get("address"),
                    "amount": balance.get("amount"),
                    "decimals": balance.get("decimals", None),
                    "price_usd": balance.get("price_usd", None),
                    "value_usd": balance.get("value_usd", None),
                    "pool_size": balance.get("pool_size", None),
                    "low_liquidity": balance.get("low_liquidity", None)
                }
                result["tokens"].append(token_data)
            
            return {"status": "success", "data": result}
        else:
            return {"status": "error", "message": "No balances found in response"}
    else:
        return {"status": "error", "message": f"API request failed with status {response.status_code}"}

def write_to_csv(data, filename="output.csv"):

    if not data["status"] == "success":
        print(f"Error: {data.get('message', 'Unknown error')}")
        return

    result = data["data"]
    
    with open(filename, mode="w", newline="", encoding='utf-8') as file:
        if result["tokens"]:
            writer = csv.DictWriter(file, fieldnames=result["tokens"][0].keys())
            writer.writeheader()
            writer.writerows(result["tokens"])
            print(f"Token data written to {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python fetch_evm_address_data.py <crypto_address>")
        sys.exit(1)

    address = sys.argv[1]

    print(f"Fetching data for address: {address}")
    result = fetch_eth_balance(address)

    if result["status"] == "success":
        print(f"Number of tokens: {result['data']['token_count']}")
        write_to_csv(result)
    else:
        print(f"Error: {result.get('message', 'Unknown error')}")

if __name__ == "__main__":
    main()