from langgraph.prebuilt import create_react_agent
from llm_model import llm_instance
from tools import multiply
from prompt import prompt

agent = create_react_agent(
    model=llm_instance,
    tools=[multiply],
    prompt=prompt
)