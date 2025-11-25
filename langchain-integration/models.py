from typing import Literal, List
from pydantic import BaseModel, Field


class MarketFactor(BaseModel):
    factor: str = Field(description="Name or short description of the market factor influencing the coin. (e.g :- ETF Approvals, Regulation news)")
    impact : str = Field(description="Explanation of how this factor affects the coins price or sentiment")

class CryptoInsight(BaseModel):
    prediction: str = Field(description="Specific prediction or insight about the coin's possible price moment or market behavior")
    confidence: int = Field(...,ge=0, le=100, description="Confidence level (0-100) indicating how strongly the prediction is supported")

class CryptoAnalysis(BaseModel):
    coin: str = Field(description="Cryptocurrency name or symbol being analyzed (e.g :- 'BTC', 'ETH')")
    summary: str = Field(description="Overall short market summary describing the current state for the coin")
    sentiment: Literal["bullish", "neutral", "bearish"] = Field(description="Overall Market sentiment for the coin based on current data")
    key_factors : List[MarketFactor] = Field(description="List of magor market factors that are currently influencing this cryptocurrency")
    insights: List[CryptoInsight] = Field(description="List of insights and predictions for this coin with confidence scores")

class CryptoAnalysisResponse(BaseModel):
    analysis: List[CryptoAnalysis] = Field(description="List of crypto analysis for each cryptocurrency")

class CryptoRequest(BaseModel):
    coins : List[str]

class CryptoComparison(BaseModel):
    winner: str
    summary: str
    reasons: List[str]

class CryptoComparisonResponse(BaseModel):
    comparison : CryptoComparison