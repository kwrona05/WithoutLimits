from fastapi import FastAPI, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import face_recognition
import numpy as np
from sqlalchemy import create_engine, Column, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pickle

# FastAPI setup
face = FastAPI()

face.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Change this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
USERS_DATABASE_URL = "sqlite:///./users.db"
Base = declarative_base()
engine = create_engine(USERS_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    face_encoding = Column(LargeBinary)


Base.metadata.create_all(bind=engine)


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# User registration
@face.post("/register")
async def register(username: str, file: UploadFile, db: SessionLocal = Depends(get_db)):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    # Load image and extract face encoding
    image = face_recognition.load_image_file(file.file)
    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) != 1:
        raise HTTPException(
            status_code=400,
            detail="Face detection error: No face or multiple faces detected",
        )

    face_encoding = face_encodings[0]
    new_user = User(username=username, face_encoding=pickle.dumps(face_encoding))
    db.add(new_user)
    db.commit()
    return {"message": "New user added to database"}


# User login
@face.post("/login")
async def login(file: UploadFile, db: SessionLocal = Depends(get_db)):
    # Load image and extract face encoding
    image = face_recognition.load_image_file(file.file)
    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) != 1:
        raise HTTPException(
            status_code=400,
            detail="Face detection error: No face or multiple faces detected",
        )

    face_encoding = face_encodings[0]
    users = db.query(User).all()

    for user in users:
        saved_encoding = pickle.loads(user.face_encoding)
        match = face_recognition.compare_faces([saved_encoding], face_encoding)

        if match[0]:
            return {"message": f"Hi, {user.username}! How are you?"}

    raise HTTPException(status_code=400, detail="Face does not match any user")