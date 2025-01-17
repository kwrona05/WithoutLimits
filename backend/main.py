from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import engine, SessionLocal
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/places", response_model=List[schemas.PlaceResponse])
def get_places(db: Session = Depends(get_db)):
    return db.query(models.Place).all()

@app.post("/places", response_model=schemas.PlaceResponse)
def creat_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = models.Place(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

@app.get("/health-data", response_model=List[schemas.HealthDataResponse])
def get_health_data(db: Session = Depends(get_db)):
    return db.query(models.HealthData).all()

@app.post("/health-data", response_model=schemas.HealthDataResponse)
def create_health_data(health_data: schemas.HealthDataCreate, db: Session = Depends(get_db)):
    db_data = models.HealthData(**health_data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data
