from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

from agno.db.sqlite import SqliteDb
import pprint

db = SqliteDb(db = "agno.db")
db.clear_memories()



def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        markdown=True,
        add_datetime_to_context=True,
        add_history_to_context= True,
        enable_user_memories=True
    )

user_id= 'pras@gmail.com'
groq_agent = build_agent()

groq_agent.print_response("what is the capital of australia", user_id=user_id)
groq_agent.print_response("what is the best time to visit it", user_id=user_id)


memories = groq_agent.get_user_memories(
    user_id=user_id
)
pprint(memories)
# agentic memory is used for complex memory management