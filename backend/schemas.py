from pydantic import BaseModel
from typing import List
from datetime import datetime

class HealthDateBase(BaseModel):
    heart_rate: int
    status: str
    timestamp: datetime

class HealthDataCreate(HealthDateBase):
    pass

class HealthDataResponse(HealthDateBase):
    id: int

    class Config:
        orm_model = True
