import asyncio
from time import sleep
from typing import List

from fastmcp import Context
from models.listinfoinput import ListInfoInput
from models.ticket import Ticket
from superops_api_calls import make_superops_graphql_request

async def get_tickets_by_criteria(input: ListInfoInput) -> List[Ticket]:
    """
        Fetches all the ticket in superops
    """
    payload = {
        "query": """
            query($listInfo: ListInfoInput!) {
                getTicketList(input: $listInfo) {
                    tickets {
                    ticketId
                    displayId
                    subject
                    source
                    followers
                    techGroup
                    technician
                    status
                    priority
                    impact
                    urgency
                    category
                    subcategory
                    cause
                    subcause
                    resolutionCode
                    sla
                    createdTime
                    updatedTime
                    firstResponseDueTime
                    firstResponseTime
                    firstResponseViolated
                    resolutionDueTime
                    resolutionTime
                    resolutionViolated
                    customFields
                    requestType
                    worklogTimespent
                    }
                }
            }
        """,
        "variables": {
            "listInfo": {
                **input.model_dump()
            }
        }
    }
    tickets_json = await make_superops_graphql_request(payload)
    return [Ticket(**t) for t in tickets_json["data"]["getTicketList"]["tickets"]]

async def get_ticket_by_userIds(userIds: List[str]):
    pass

async def get_all_departments():
    """
        Fetches all the department available in the company.

    """
    payload = {
        "query": """
            query {
                getDepartmentList {
                    departmentId 
                    name
                    head
                }
            }
        """
    }

    return await make_superops_graphql_request(payload)



    

