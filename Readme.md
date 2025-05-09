# Elliptic Screening

A Python tool for fetching and writing token balances and metadata for EVM addresses using the Dune API.

## Overview

This tool allows you to fetch detailed token balance information for any EVM address, including:
- Token balances across different chains
- Token metadata (symbol, name, decimals)
- USD values and prices
- Liquidity information

The tool automatically filters out spam tokens and tokens with low liquidity (less than $100 of onchain liquidity).

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/miguelcores/elliptic-screening.git
cd elliptic-screening
```

2. Install the required dependencies:
```bash
pip install requests
```

## Usage

Run the script from the command line by providing an Ethereum address:

```bash
python fetch_evm_address_data.py <ethereum_address>
```

For example:
```bash
python fetch_evm_address_data.py 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
```

The script will:
1. Fetch token balances and metadata for the provided address
2. Filter out spam tokens and low liquidity tokens
3. Generate a CSV file (`output.csv`) with the following information for each token:
   - Chain and chain ID
   - Token symbol and name
   - Token address
   - Balance amount
   - Token Decimals
   - USD price and value
   - Pool size
   - Low liquidity flag

## Output Format

The generated CSV file contains the following columns:
- `chain`: The blockchain network
- `chain_id`: The chain identifier
- `symbol`: Token symbol
- `name`: Token name
- `address`: Token contract address
- `amount`: Token balance
- `decimals`: Token decimals
- `price_usd`: Current USD price
- `value_usd`: Total value in USD
- `pool_size`: Size of the liquidity pool
- `low_liquidity`: Flag indicating low liquidity

## API Key

The script uses the Dune API. You can replace the `API_KEY` in the script with your own Dune API key.
