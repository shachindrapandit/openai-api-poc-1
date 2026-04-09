from fastapi import FastAPI
from pydantic import BaseModel
from mcp_client import call_tool
from ollama_client import ask_llm

app = FastAPI()

class Request(BaseModel):
    message: str


def decide_tool(user_input: str):
    prompt = f"""
You are an AI assistant.

Decide if the user input requires a tool.

Available tool:
- calculator (for math expressions)

Respond ONLY in JSON:

If tool needed:
{{"tool": "calculator", "input": "<expression>"}}

If no tool:
{{"tool": "none"}}

User input: {user_input}
"""

    response = ask_llm(prompt)
    return response


@app.post("/chat")
def chat(req: Request):
    user_input = req.message

    decision = decide_tool(user_input)

    # 🧠 Basic parsing (improve later)
    if "calculator" in decision:
        try:
            expr = decision.split("input")[1].split(":")[1].strip().replace('"', '').replace("}", "")
        except:
            expr = user_input

        tool_result = call_tool("calculator", expr)

        # 👉 Send result back to AI for final answer
        final_prompt = f"""
User asked: {user_input}
Tool result: {tool_result}

Generate a helpful final response.
"""
        final_response = ask_llm(final_prompt)

        return {
            "flow": "AI + MCP",
            "decision": decision,
            "tool_result": tool_result,
            "final": final_response
        }

    # 👉 No tool needed
    normal_response = ask_llm(user_input)

    return {
        "flow": "AI only",
        "response": normal_response
    }