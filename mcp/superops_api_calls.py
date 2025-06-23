import httpx
import os

# TODO: move this env
auth_token = os.getenv("AUTH_TOKEN")
customer_subdomain = os.getenv("CUSTOMER_SUBDOMAIN")
url = "https://api.superopsalpha.com/it"
headers = {
        "Authorization": f"Bearer {auth_token}",
        "CustomerSubDomain": customer_subdomain,
        "Content-Type": "application/json"
    }


async def make_superops_graphql_request(payload: dict | None):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            headers=httpx.Headers(headers),
            json=payload
        )
        return response.json()

    