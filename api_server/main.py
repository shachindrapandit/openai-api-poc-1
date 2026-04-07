from fastapi import FastAPI
from pydantic import BaseModel
from mcp_client import call_tool

app = FastAPI()

class Request(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Request):
    user_input = req.message

    # 👇 MCP Client decides tool (simple logic)
    if "calculate" in user_input:
        expr = user_input.replace("calculate.", "").strip()

        result = call_tool("calculator", expr)

        return {
            "flow": "MCP",
            "tool": "calculator",
            "input": expr,
            "output": result
        }

    return {
        "flow": "direct",
        "message": "No tool needed.."
    }
