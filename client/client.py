import os
import traceback
import json
import requests
from contextlib import AsyncExitStack
from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.types import ContentBlock
from mcp.client.streamable_http import streamablehttp_client
from logger import logger

load_dotenv()

class tool_mapping:
    def __init__(self, tool_name, tool_description, tool_inputSchema, server_url, protocol):
        self.tool_name = tool_name
        self.tool_description = tool_description
        self.tool_inputSchema = tool_inputSchema
        self.server_url = server_url
        self.protocol = protocol

class response_mapping:
    def __init__(self, satus, response_content, response_type):
        self.status = satus
        self.response_content = response_content
        self.response_type = response_type

class MCPClient:
    def __init__(self):
        self.tools = []
        self.tool_mappings:list[tool_mapping] = []
        self.messages = []
        self.logger = logger
        self.model_name = os.getenv('MODEL_NAME')
        self.api_key = os.getenv('GROQ_API_KEY')
        self.llm_api_url = os.getenv('LLM_API_URL')

    def load_config(self,config_file:str="./mcpserver_config.json")-> dict:
        try:    
            with open(config_file, 'r') as file:
                config = json.load(file)
            self.logger.info("MCP Server configuration loaded successfully.",config)    
            return config
        except Exception as e:
            self.logger.error(f"⚠️  Could not load configuration: {e}")  
            traceback.print_exc()
            raise     

    '''
        this method is used to load tools from the MCP server using Streamable HTTP protocol
    '''
    async def load_tools_streamable_http(self, server_url: str):
        local_exit_stack = AsyncExitStack()
        transport = await local_exit_stack.enter_async_context(
                streamablehttp_client(server_url)
            )
        read, write ,_ = transport
        session = await local_exit_stack.enter_async_context(
            ClientSession(read, write)
        )
        await session.initialize()
        self.logger.info(f"Connected to MCP server: {server_url}")
        
        try:
            response = await session.list_tools()
            for tool in response.tools:
                self.tool_mappings.append(
                    tool_mapping(
                        tool_name=tool.name,
                        tool_description=tool.description,
                        tool_inputSchema=tool.inputSchema,
                        server_url=server_url,
                        protocol='streamable_http'
                    )
                )
            
        except Exception as e:
            self.logger.error(f"⚠️  Could not load tools: {e}")  
            traceback.print_exc()
            raise
        finally:
            await local_exit_stack.aclose()
            self.logger.info(f"Disconnected from MCP server: {server_url}")

    
    '''
        this method is used to load tools from the MCP server using SSE protocol
    '''
    async def load_tools_sse(self, server_url: str):
        local_exit_stack = AsyncExitStack()
        transport = await local_exit_stack.enter_async_context(
                sse_client(server_url)
            )
        read, write = transport
        session = await local_exit_stack.enter_async_context(
            ClientSession(read, write)
        )
        await session.initialize()
        self.logger.info(f"Connected to MCP server: {server_url}")

        
        try:
            response = await session.list_tools()
            for tool in response.tools:
                self.tool_mappings.append(
                    tool_mapping(
                        tool_name=tool.name,
                        tool_description=tool.description,
                        tool_inputSchema=tool.inputSchema,
                        server_url=server_url,
                        protocol='sse'
                    )
                )
                
            
        except Exception as e:
            print(f"⚠️  Could not load tools: {e}")
            self.logger.error(f"⚠️  Could not load tools: {e}")  
            traceback.print_exc()
            raise
        finally:
            await local_exit_stack.aclose()
            self.logger.info(f"Disconnected from MCP server: {server_url}")

    '''
        Load tools from all MCP Servers (whose urs are defined in ./mcpserver_config.json)
    '''
    async def load_tools(self):
        try: 
            tool_configs = self.load_config()
            for service, details in tool_configs.items():
                server_url = details['url']
                protocol = details['transport']
                if protocol == "sse":
                    await self.load_tools_sse(server_url)
                elif protocol == "streamable_http":
                    await self.load_tools_streamable_http(server_url)
                else:
                    self.logger.error(f"Unsupported protocol : {protocol}")
        except Exception as e:
            self.logger.error(f"⚠️  Could not load tools: {e}")  
            traceback.print_exc()        
               
    
    
    async def tool_call(self, responseMapping: response_mapping):
        tool_name = responseMapping.response_content[0]['function']['name']
        input_data_str = responseMapping.response_content[0]['function']['arguments']
        server_url = ""
        protocol = ""
        
        if isinstance(input_data_str, str):
            try:
                input_data = json.loads(input_data_str)
            except Exception as e:
                self.logger.error(f"⚠️  Could not parse tool arguments as JSON: {input_data_str}")
                raise
        
        # find the tool mapping for the tool name
        for tool in self.tool_mappings:
            if tool.tool_name == tool_name:
                server_url = tool.server_url
                protocol = tool.protocol
                break
        
        self.logger.info(f"Calling tool: {tool_name} \n with input: {input_data} \n using protocol: {protocol} and server URL: {server_url}")


        if protocol == "streamable_http":
            local_exit_stack = AsyncExitStack()
            transport = await local_exit_stack.enter_async_context(
                    streamablehttp_client(server_url)
                )
            read, write ,_ = transport
            session = await local_exit_stack.enter_async_context(
                ClientSession(read, write)
            )
            await session.initialize()
            result= await session.call_tool(tool_name, input_data)
            self.logger.info(f"Tool {tool_name} result: {result}...")
            await local_exit_stack.aclose()
            return result
        elif protocol == "sse":
            local_exit_stack = AsyncExitStack()
            transport = await local_exit_stack.enter_async_context(
                    sse_client(server_url)
                )
            read, write = transport
            session = await local_exit_stack.enter_async_context(
                ClientSession(read, write)
            )
            await session.initialize()
            result= await session.call_tool(tool_name, input_data)
            self.logger.info(f"Tool {tool_name} result: {result}...")
            await local_exit_stack.aclose()
            return result
        else:
            self.logger.error(f"⚠️  Unsupported protocol: {protocol}")
            raise Exception(f"Unsupported protocol: {protocol}")

    async def llm_call(self):
        url = self.llm_api_url
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }   
        
        data = {
            "model": self.model_name,
            "messages": self.messages,
            "temperature": 1,
            "max_completion_tokens": 1000,
            "top_p": 1,
            "tools": self.convert_mcp_tools_to_groq_format() 
        }

        self.logger.debug("################### Calling Groq API with data #######################")
        self.logger.debug(json.dumps(data, indent=2))
        self.logger.debug("##########################################")

        return requests.post(url, headers=headers, json=data)

    
    async def execute_query(self, query: str):
        user_message = {"role": "user", "content": query}
        self.messages = [user_message]
        while True:
            response = await self.llm_call()
            formatted_response = self.map_llm_output_response(response)
            
            if formatted_response.response_type == "content":
                assistant_message = {
                        "role": "assistant",
                        "content": formatted_response.response_content,
                    }
                self.messages.append(assistant_message)
                break
            elif formatted_response.response_type == "tool_calls":
                tool_call_response = await self.tool_call(formatted_response)
                response_blocks: list[ContentBlock] = tool_call_response.content
                payload = [block.model_dump() for block in response_blocks]
                
                tool_call_message = {
                    "role": "user",
                    "content": payload
                }

                self.messages.append(tool_call_message)
                # self.logger.info("Tool call message:", self.messages)
        return self.messages
    
    def map_llm_output_response(self, response)->response_mapping:
        if response.status_code != 200:
            raise Exception(f"Error calling Groq API: {response.status_code} - {response.text}")
        response_data = response.json()
        if 'choices' not in response_data or len(response_data['choices']) == 0:
            raise Exception("Invalid response from Groq API: No choices found")
        message = response_data['choices'][0]['message']
        
        if "tool_calls" in message and message["tool_calls"]:
            response_type = "tool_calls" 
            return response_mapping(
                satus=response.status_code,
                response_content=message['tool_calls'],
                response_type=response_type
            )
        elif "content" in message and message["content"]:
            response_type = "content" 
            return response_mapping(
                satus=response.status_code,
                response_content=message['content'],
                response_type=response_type
            )
        else:    
            return response_mapping(
                satus=response.status_code,
                response_content=None,
                response_type=None
            ) 
    
    def convert_mcp_tools_to_groq_format(self):
        groq_tools = []
        for tool in self.tool_mappings:
            groq_tool = {
                "type": "function",
                "function": {
                    "name": tool.tool_name,
                    "description": tool.tool_description,
                    "parameters": tool.tool_inputSchema
                }
            }
            groq_tools.append(groq_tool)
        return groq_tools


def find_assitant_message(messages):
    first_assistant_message = next((msg for msg in messages if msg.get("role") == "assistant"), None)
    if first_assistant_message and first_assistant_message.get('content') is not None:
        return first_assistant_message['content']
    return None 


if __name__ == "__main__":
    import asyncio
    client = MCPClient()
    asyncio.run(client.load_tools())
    query = "my fist name is John plsease list my orders"
    llm_output = asyncio.run(client.execute_query(query))
    print("Messages:", find_assitant_message(llm_output))

    
