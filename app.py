from agent import agent
from langchain_core.messages import HumanMessage, AIMessage

print("\n******STARTING APP******\n")

user_input = "what's of 2 * 4 ??"
print(f"User input: {user_input}")

# LangGraph expects messages format
response = agent.invoke({"messages": [HumanMessage(content=user_input)]})

# Extract only the final assistant message content
final_response = ""
for msg in response["messages"]:
    if isinstance(msg, AIMessage) and msg.content:
        final_response = msg.content

print(f"Response: {final_response}")

print("\n******End of Agent Response******\n")