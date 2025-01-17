from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.dialects.postgresql import JSON
from database import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    accessibility_features = Column(JSON)

    class HealtData(Base):
        __tablename__ = "health_date"

        id = Column(Integer, primary_key=True, index=True)
        heart_rate = Column(Integer, nullable=False)
        timestamp = Column(String, nullable=False)
