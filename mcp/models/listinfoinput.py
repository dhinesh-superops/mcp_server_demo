from typing import List, Optional, Union
from pydantic import BaseModel

class RuleConditionInput(BaseModel):
    joinOperator: Optional[str] = None
    operands: Optional[List['RuleConditionInput']] = None
    attribute: Optional[str] = None
    operator: Optional[str] = None
    value: Optional[Union[dict, list, str, int, float, bool, None]] = None

class SortInput(BaseModel):
    # Adjust fields as per your actual SortInput definition
    field: str
    direction: str

class ListInfoInput(BaseModel):
    page: Optional[int] = None
    pageSize: Optional[int] = None
    condition: Optional[RuleConditionInput] = None
    sort: Optional[List[SortInput]] = None
