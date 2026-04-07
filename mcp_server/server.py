from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToolRequest(BaseModel):
    tool: str
    input: str

@app.post("/execute")
def execute_tool(req: ToolRequest):
    
    if req.tool == "calculator":
        try:
            result = eval(req.input)
            return {"result": str(result)}
        except Exception as e:
            return {"error": str(e)}

    return {"error": "Unknown tool.."}