from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel): 
    title:str
    description:str
    is_completed:bool
    is_deleted:bool
    updated_at: int = int(datetime.timestamp(datetime.now()))
    creation: int = int(datetime.timestamp(datetime.now()))