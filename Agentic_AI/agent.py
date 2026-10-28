from agno.agent import Agent

#from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv

#import websearch tool

from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        markdown=True,

        tools = [DuckDuckGoTools()], # gave acccess to a websearch tool
        instructions = "you are a helpful and expert travel agent",
        add_datetime_to_context=True,
    )

groq_agent = build_agent()

groq_agent.print_response("should i travel to israel, is it safe?")