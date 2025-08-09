from mcp.server.fastmcp import FastMCP

mcp = FastMCP("email_service")

@mcp.tool()
async def send_email(toEmailAddress: str, orderDeatils: str) -> str:
    """Sends an email with the specified odersDeatils to the given recipients email address"""
    # Simulate sending an email
    with open(f"sent_email_to_{toEmailAddress}.txt", "w") as f:
        f.write(f"To: {toEmailAddress}\nOrder Details: {orderDeatils}\n")
    return f"Email sent to {toEmailAddress} with and body '{orderDeatils}'."

if __name__ == "__main__":
    mcp.run(transport='streamable-http')