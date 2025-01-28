from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class HealthData(Base): 
    __tablename__ = "health_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    heart_rate = Column(Integer, nullable=False)
    status = Column(String, nullable=False)