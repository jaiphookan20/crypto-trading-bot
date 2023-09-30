from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config # allows us to access env variables
from dydx3.constants import NETWORK_ID_GOERLI
from dydx3.constants import NETWORK_ID_MAINNET


# !!!! SELECT MODE !!!!!
MODE = "DEVELOPMENT"

# Close all open positions & orders
ABORT_ALL_POSITIONS=True

# Find Cointegrated Pairs
FIND_COINTEGRATED = True

# Place Trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "1HOUR"

# Stats Window // for our rolling avg, we'll use 21 days
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1880 # if in prod, you'd want to put an amount that corresponds close to the amount you have in your account, this is because we don't want the bot to keep opening trades. By specifying an amount close to the amount you have, it specifies that this is the amount it's allowed to have before its allowed to go and open trades

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True # if Z score is at -1.5 or more it'll open that trade, and if it crosses +1.5 it'll close it

ETHEREUM_ADDRESS = "0x757f7E2b25098F6FF426E5189b132561a638Cc31"

# Wallet Private Key
ETH_PRIVATE_KEY = "0x323dae3abfbce7eca9116d241ecb13b64a166acb242867f5c79aa79e9f6d2f34"

# KEYS - Production
# Must remember to be on Mainnet on DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET =  config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET=config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# KEYS - Development
# Must be on Testnet on DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET =config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET=config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET =config("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET= DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

# HOST - Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_GOERLI

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/zsxLDAMUHDaZLJMWWA915hVxHJM8VHyI"
HTTP_PROVIDER_TESTNET = "https://eth-mainnet.g.alchemy.com/v2/XbPzE4EfewMjjF0T08AYEzD3HwvWJIa9"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET

# NETWORK ID - Export
NETWORK_ID = NETWORK_ID_MAINNET if MODE == "PRODUCTION" else NETWORK_ID_GOERLI