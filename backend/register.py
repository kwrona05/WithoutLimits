from fastapi import FastAPI, UploadFile, HTTPException
import face_recognition
import numpy as np
import cv2
from sqlalchemy import create_engine, Column, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

face = FastAPI()

#Users database congifuration
USERS_DATABASE_URL = "sqlite:///.users.db"
Base = declarative_base()
engine = create_engine(USERS_DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    face_encoding = Column(LargeBinary)

Base.metadata.create_all(bind=engine)

#Users register
@face.post("/register")
async def register(username: str, file: UploadFile):
    session = SessionLocal()
    if session.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    
    image = face_recognition.load_image_file(file.file)
    face_encoding = face_recognition.face_encoding(image)

    if len(face_encoding) != 1:
        raise HTTPException(status_code=400, detail="No face or few faces detected")
    
    face_encoding = face_encoding[0]
    new_user = User(username=username, face_encoding=face_encoding.tobytes())
    session.add(new_user)
    session.commit()
    session.close()
    return {"message": "New user added to database"}

#User login
@face.post("/login")
async def login(file: UploadFile):
    session = SessionLocal()
    image = face_recognition.load_image_file(file.file)
    face_encoding = face_recognition.face_encoding(image)

    if len(face_encoding) != 1:
        raise HTTPException(status_code=400, detail="No face or few faces detected")
    
    face_encoding = face_encoding[0]
    users = session.query(User).all()

    for user in users:
        save_encoding = np.frombuffer(user.face_encoding, dtype=np.float64)
        match = face_recognition.compare_faces([save_encoding], face_encoding)

        if match[0]:
            session.close()
            return {"message": f"Hi, {user.username} how are you?"}
        
    session.close()
    raise HTTPException(status_code=400, detail="Face isn't fit to any user")