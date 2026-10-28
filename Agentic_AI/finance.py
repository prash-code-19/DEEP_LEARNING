from agno.agent import Agent

#from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv

#import websearch tool
from agno.tools.duckduckgo import DuckDuckGoTools

#import finance tool
from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        markdown=True,

        tools = [DuckDuckGoTools(), YFinanceTools()], # gave acccess to a websearch tool
        add_datetime_to_context=True,

        description= "You are an investment analyst that researches stock prices, analyst recommendations and stock fundamentals",
        instructions=["format your responses using markdown and use tables to display data where possible"],

        debug_mode=True # we get a lot of background information
    )

groq_agent = build_agent()

groq_agent.print_response("stock price of nvda and analyst recommendations")