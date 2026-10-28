from agno.agent import Agent

#from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

from agno.team import Team

eng_agent = Agent(name="English Agent", role = "You answer questions in English")
hind_agent = Agent(name="Hindi Agent", role = "You answer questions in Hindi")
chi_agent = Agent(name="Chinese Agent", role = "You answer questions in chinese")


team_leader = Team(
    name = "Answer and translation Team",
    members = [eng_agent, hind_agent, chi_agent],
    model=Groq(id="llama-3.1-8b-instant"),
    markdown = True,
    show_members_responses =True,
    instructions = """All members must respond to the query in their specific language
                        do not route to just one agent
                        output all the responses
                    """
)


team_leader.print_response("what is capital of India")