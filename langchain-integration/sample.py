import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
OPENROUTER_URL = os.getenv("OPENROUTER_URL")
COINGECKO_URL= os.getenv("COINGECKO_URL")




chat_prompt = ChatPromptTemplate.from_template(
    """
    You are a expert humorous poem writer

    You will be give a word as input, Then you should write a humorous poem for it

    Below is the word
    {word}
    """
)

llm = ChatOpenAI(model="meta-llama/llama-3.3-70b-instruct:free",
                 base_url=OPENROUTER_URL, api_key=OPENROUTER_KEY)

response_chain = chat_prompt | llm

resp = response_chain.invoke({"word": "Maithripala Sirisena"})

print(resp.content)