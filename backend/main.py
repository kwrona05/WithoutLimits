from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import engine, SessionLocal
import models
import schemas
import random
import datetime
from fastapi.middleware.cors import CORSMiddleware

# Inicjalizacja FastAPI
app = FastAPI()

# Middleware dla CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dostosuj do swoich potrzeb w produkcji
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Funkcja dla połączenia z bazą danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint POST /heartrate
@app.post('/heartrate', response_model=schemas.HealthDataResponse)
def create_heart_rate(db: Session = Depends(get_db)):
    heart_rate = random.randint(60, 120)
    status = "normal" if heart_rate <= 90 else "high"
    new_heart_rate = models.HealthData(  # Sprawdź nazwę klasy
        heart_rate=heart_rate,
        status=status,
        timestamp=datetime.datetime.now(),  # Popraw import
    )
    db.add(new_heart_rate)
    db.commit()
    db.refresh(new_heart_rate)
    return new_heart_rate

# Endpoint GET /heartrates
@app.get("/heartrates", response_model=List[schemas.HealthDataResponse])
def get_heart_rates(db: Session = Depends(get_db)):
    heart_rates = db.query(models.HealthData).all()
    return heart_rates