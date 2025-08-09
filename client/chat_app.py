import streamlit as st
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="qwen/qwen3-32b")

def load_config(config_file:str="./mcpserver_config.json")-> dict:
        import json
        with open(config_file, 'r') as file:
            config = json.load(file)
        print("MCP Server configuration loaded:", config)    
        return config

async def run(user_input:str):
    #load_dotenv()
    print("Hello from mcp-langchain!")
    client=MultiServerMCPClient(
        load_config("./mcpserver_config.json")
    )

    print("client created")
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    print("client api")
    tools = await client.get_tools()
    print("client tools")
    #model = ChatGroq(model="qwen/qwen3-32b")
    print("model created")
    agent = create_react_agent(
        model=model,
        tools=tools
    )
    print("agent created")
    math_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                    #"content": "my userid is user1 can you list all my orders?"
                    #"content": "my fist name is John, can you list all my orders?"
                }
            ]
        }
        )
    print("math response received")
    #print("Weather response:", math_response['messages'][-1].content)
    st.write(math_response['messages'][-1].content)
    #return math_response['messages'][-1].content


st.title("MCP Chat Client")

# Text input for user message
user_input = st.text_input("Enter your message:")

# Button to send message
if st.button("Send"):
    #client = mcp_client()
    # Run the async method in the Streamlit event loop
    response = asyncio.run(run(user_input))
    #st.write("Response from MCP Client:")
    #st.write(response)