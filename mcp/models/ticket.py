from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class Ticket(BaseModel):
    ticketId: str = Field(..., description="The ID of the ticket.")
    displayId: str = Field(..., description="The system-generated, human-readable ID of the ticket.")
    subject: str = Field(..., description="The subject of the ticket.")

    ticketType: Optional[str] = Field(
        default=None,
        description="The type of the ticket. Deprecated: As Ticket Type value is customizable, instead of this field, requestType field will have the value."
    )

    source: str = Field(..., description="The creation source of the ticket.")

    client: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The client to whom the ticket is associated. Returns accountId and name fields as JSON."
    )

    site: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The site to which the ticket is associated. Returns ID and name fields as JSON."
    )

    requester: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The client user for whom the ticket is created. Returns userId and name fields as JSON."
    )

    additionalRequester: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="The list of client users who act as additional requesters. Each object contains userId and name."
    )

    followers: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="The list of technicians who follow the ticket. Each object contains userId and name."
    )

    techGroup: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The technician group to which the ticket is assigned. Returns groupId and name fields as JSON."
    )

    technician: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The technician to whom the ticket is assigned. Returns userId and name fields as JSON."
    )

    status: Optional[str] = Field(
        default=None,
        description="The status of the ticket."
    )

    approvalStatus: Optional[str] = Field(
        default=None,
        description="The approval status of the ticket."
    )

    priority: Optional[str] = Field(
        default=None,
        description="The priority of the ticket."
    )

    impact: Optional[str] = Field(
        default=None,
        description="The impact of the ticket."
    )

    urgency: Optional[str] = Field(
        default=None,
        description="The urgency of the ticket."
    )

    category: Optional[str] = Field(
        default=None,
        description="The category of the ticket."
    )

    subcategory: Optional[str] = Field(
        default=None,
        description="The subcategory of the ticket."
    )

    cause: Optional[str] = Field(
        default=None,
        description="The cause of the ticket."
    )

    subcause: Optional[str] = Field(
        default=None,
        description="The sub cause of the ticket."
    )

    resolutionCode: Optional[str] = Field(
        default=None,
        description="The resolution code of the ticket."
    )

    sla: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The SLA of the ticket. Returns id and name fields as JSON."
    )

    createdTime: Optional[str] = Field(
        default=None,
        description="The time when the ticket was created."
    )

    updatedTime: Optional[str] = Field(
        default=None,
        description="The time when the ticket was updated."
    )

    firstResponseDueTime: Optional[str] = Field(
        default=None,
        description="The due time of first response metric."
    )

    firstResponseTime: Optional[str] = Field(
        default=None,
        description="The first response time of the ticket."
    )

    firstResponseViolated: Optional[bool] = Field(
        default=None,
        description="Denotes whether the first response metric is violated."
    )

    resolutionDueTime: Optional[str] = Field(
        default=None,
        description="The due time of resolution metric."
    )

    resolutionTime: Optional[str] = Field(
        default=None,
        description="The resolution time of the ticket."
    )

    resolutionViolated: Optional[bool] = Field(
        default=None,
        description="Denotes whether the resolution metric is violated."
    )

    customFields: Optional[Dict[str, Any]] = Field(
        default=None,
        description=(
            "Specifies the custom field values for the ticket. Each entry in the JSON is a key-value pair. "
            "The key will be the system-generated column name. Text, paragraph, radio, etc. are strings. "
            "Checkbox, multi-select are arrays of strings."
        )
    )

    requestType: Optional[str] = Field(
        default=None,
        description="Specifies the type of the ticket."
    )
