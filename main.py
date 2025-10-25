import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.api_client import ApiClient
from plaid.configuration import Configuration



PLAID_CLIENT_ID="68fd03e0c77fc80023aaf819"
PLAID_APIKEY="6c04d90516515b7a6e344107ae852d"

load_dotenv()

client_id = os.getenv("PLAID_CLIENT_ID")
secret = os.getenv("PLAID_SECRET")

configuration = Configuration(
    host="https://sandbox.plaid.com",
    api_key={"clientId": client_id, "secret": secret}
)

client = plaid_api.PlaidApi(ApiClient(configuration))