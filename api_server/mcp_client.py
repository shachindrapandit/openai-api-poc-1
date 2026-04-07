import requests

MCP_SERVER_URL = "http://127.0.0.1:9000/execute"

def call_tool(tool, input_data):
    response = requests.post(
        MCP_SERVER_URL,
        json={
            "tool": tool,
            "input": input_data
        }
    )
    return response.json()
