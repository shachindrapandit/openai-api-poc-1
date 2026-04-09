Postman → API Server → AI (Ollama) → MCP Client → MCP Server → Tool → Back → AI → Response

System Workflow

The API receives user input and forwards it to the AI.
The AI analyzes the request to determine its type (e.g., plain English query or mathematical problem).
If the request is identified as a mathematical problem, the API interprets the AI’s decision and invokes the MCP client.
The MCP server processes the request and returns the computed result.
The API receives the result from the MCP server and sends it back to the AI.
The AI transforms the raw output into a clear, human-friendly response.