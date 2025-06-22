import asyncio
from fastmcp import FastMCP, Context
from fastmcp.prompts import Prompt
from fastmcp.server.dependencies import get_context

from fastmcp.resources import Resource
from prompts.test import generate_code_request
from resources.test import get_greeting
from tools.ticketing import get_tickets_by_criteria, get_all_departments

tools = [
    get_tickets_by_criteria,
    get_all_departments
]

mcp = FastMCP(
            name="superops-mcp", 
            instructions="This server serves tools to interact with superops SaaS application",
            tools=tools
            )

@mcp.tool
async def process_items(items: list[str], ctx: Context) -> dict:
    """Process a list of items with progress updates."""
    total = len(items)
    results = []

    
    for i, item in enumerate(items):
        # Report progress as percentage

        await ctx.log("In Progress----")
        await ctx.report_progress(progress=i,message="Processing", total=total)
        
        # Process the item (simulated with a sleep)
        await asyncio.sleep(2)
        results.append(item.upper())
    
    # Report 100% completion
    await ctx.report_progress(progress=total,message="Processing Done", total=total)
    
    return {"processed": len(results), "results": results}

@mcp.tool
async def example_tool(prompt: str, context: Context) -> str:
    """Sample a completion from the LLM."""
    response = await context.sample(
        "What is your favorite programming language?",
        system_prompt="You love languages named after snakes.",
    )
    print(response)
    # assert isinstance(response, TextContent)
    return response.text

mcp.add_resource(Resource.from_function(get_greeting, "resource://greeting"))
mcp.add_prompt(Prompt.from_function(generate_code_request,"generate_code_request"))

# async def main():
#     # Use run_async() in async contexts
#     await mcp.run_async(transport="streamable-http", port=3001)

if __name__ == "__main__":
    # mcp.run(transport="streamable-http", port=3001)
    mcp.run(transport="stdio")
    # asyncio.run(main())

