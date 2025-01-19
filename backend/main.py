from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import engine, SessionLocal
import models
import schemas
import random
import datetime

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

@app.get("/heartrate")
def get_pseudo_hearrate():
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "heart_rate": random.randint(60, 120),
        "status": "normal" if random.randint(60, 120) <= 90 else "high"
    }

