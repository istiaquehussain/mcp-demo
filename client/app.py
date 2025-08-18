import streamlit as st
from dotenv import load_dotenv
import client as clt
import asyncio

load_dotenv()

client = clt.MCPClient()
asyncio.run(client.load_tools())


st.title("MCP Chat Client")

# Text input for user message
user_input = st.text_input("Enter your message:")

# Button to send message
if st.button("Send"):
    llm_output = asyncio.run(client.execute_query(user_input))
    st.write(clt.find_assitant_message(llm_output))
    