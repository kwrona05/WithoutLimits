from pydantic import BaseModel
from typing import List

class PlaceBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    accessibility_features: List[str]

class PlaceCreate(PlaceBase):
    pass

class PlaceResponse(PlaceBase):
    id: int

    class Config:
        orm_model = True

class HealthDateBase(BaseModel):
    heart_rate: int
    timestamp: str

class HealthDataCreate(HealthDateBase):
    pass

class HealthDataResponse(HealthDateBase):
    id: int

    class Config:
        orm_model = True
