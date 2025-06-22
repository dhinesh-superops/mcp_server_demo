
import httpx

# TODO: move this env
auth_token: str = "api-eyJhbGciOiJSUzI1NiJ9.eyJqdGkiOiI0Mjk1OTEwMzE0NjIzMTUyMTI4IiwicmFuZG9taXplciI6Ilx1MDAwNO-_vTbvv70_77-977-9NkLvv70ifQ.GOxAt3hixJz6aGgDypZjAppfh0lea1iguw8FlqIZejaMa8QuOKWQadEozofrGbP3esN8ghmC6_iXVaq_loShUndNa1Dyy8sLTNNbTz3S5sl-6JGYGlK2ds3wQxMW_mQX6upotPS94iWOlEeAMWkS2Ttl_b75Vm_Aw2Uiw0tpKIzyAWH9zqd3ICKXHUuAkzErAp1vTDf2tn6M5IJWkx3q35uA9uJam6R9X-YQ_F00I3dvl3yLQtpCt8-ahw_62GCXv02HKCWrmo3lFiFT6nnWg9JgIE4AB4dxk1Gqzoi7B3YtkQfqqm7xYgHca-lQKO_rLpRYN-t8Wa2i2958tkeIpQ"
customer_subdomain: str = "devsupropsit20"
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

    