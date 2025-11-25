import json
import os
from typing import List
import requests
from fastapi import HTTPException, FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from starlette import status

from models import CryptoAnalysisResponse,CryptoRequest

load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
OPENROUTER_URL = os.getenv("OPENROUTER_URL")
COINGECKO_URL= os.getenv("COINGECKO_URL")

app = FastAPI(description="AI powered crypto Analysis API")

def get_crypto_data(coin_list: List[str]):
    if not coin_list:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No coins provided")

    coins = ",".join(coin_list)

    params = {
        "vs_currency": "usd",
        "ids": coins
    }
    crypto_api_repo = requests.get(COINGECKO_URL, params=params)
    return crypto_api_repo.json()


def get_crypto_analysis_response(coins: List[str]):

    chat_prompt = ChatPromptTemplate.from_template(
            """
       You are a "CryptoAnalyst - AI" a professional cryptocurrency market analyst
       
       You will be given recent market data for multiple cryptocurrencies (price, market cap, volume, 24h change)
       Here is market data :
       {market_data}
       
       Rules:
       - Return one analysis per cryptocurrency
       - Provide 3 key_factory and 3 insights per coin
       -Base you reasoning on given metric (e.g price change market cap trend)
       
       
       """
        )
    llm = ChatOpenAI(model="meta-llama/llama-3.3-70b-instruct:free",
                         base_url=OPENROUTER_URL, api_key=OPENROUTER_KEY).with_structured_output(CryptoAnalysisResponse)
    response_chain = chat_prompt | llm
    resp = response_chain.invoke({"market_data": json.dumps(get_crypto_data(coins))})
    return resp
@app.post("/crypto/analysis")
def analyze_crypro(request : CryptoRequest):
    return get_crypto_analysis_response(request.coins)
