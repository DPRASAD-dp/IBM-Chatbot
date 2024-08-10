
from ibm_watson import IAMTokenManager

# In your API endpoint use this to generate new bearer tokens
iam_token_manager = IAMTokenManager(apikey='Enter your API key here.')
token = iam_token_manager.get_token()

print("Generated Token:", token)