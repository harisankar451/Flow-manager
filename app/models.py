from pydantic import BaseModel
from typing import List, Optional

class TaskSchema(BaseModel):
    name: str
    description: Optional[str] = None 

class ConditionSchema(BaseModel):
    name: str 
    source_task: str 
    outcome: str
    target_task_success: str 
    target_task_failure: str

class FlowSchema(BaseModel):
    id: str 
    name: str
    start_task: str
    tasks: List[TaskSchema] 
    conditions: List[ConditionSchema] 

class FlowRequest(BaseModel):
    flow: FlowSchema 