from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a multiplication assistant. Extract the numbers from the user's input and use the multiply tool with those exact numbers. Do not use any other numbers."),
    ("placeholder", "{messages}")
])