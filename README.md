To run, set AUTH_TOKEN, CUSTOMER_SUBDOMAIN in environment

For STDIO, 
- replace this line at the end in main.py
```
if __name__ == "__main__":
	mcp.run(transport="stdio")
```
- add this configuration to the claude
```
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
              "/Users/dhineshl/superops-mcp/mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

- For remote server and making calls with it, make this change in main.py at the end
```
if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=3001)
```

- run this to inspect and make calls to the remote mcp
`npx @modelcontextprotocol/inspector`

