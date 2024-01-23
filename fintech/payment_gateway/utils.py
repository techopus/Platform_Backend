# created for API key setup
# payment_gateway/utils.py

import openai
from django.conf import settings

def setup_openai_api_key():
    openai.api_key = settings.OPENAI_API_KEY
