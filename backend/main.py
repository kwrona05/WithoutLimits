from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import engine, SessionLocal
import models
import schemas
import random
import datetime
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/heartrate', response_model=schemas.HealthDataResponse)
def create_heart_rate(db: Session = Depends(get_db)):
    heart_rate = random.randint(60, 120)
    status = "normal" if heart_rate <= 90 else "high"
    new_heart_rate = models.HealtData(
        heart_rate = heart_rate,
        status=status,
        timestamp=datetime.now(),
    )
    db.add(new_heart_rate)
    db.commit()
    db.refresh(new_heart_rate)
    return new_heart_rate

@app.get("/heartrates", response_model=List[schemas.HealthDataResponse])
def get_heart_rates(db: Session = Depends(get_db)):
    heart_rates = db.query(models.HealthData).all()
    return heart_rates