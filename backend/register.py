from fastapi import FastAPI, UploadFile, HTTPException, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
import face_recognition
from PIL import UnidentifiedImageError
from sqlalchemy import create_engine, Column, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pickle
import logging

# FastAPI setup
face = FastAPI()

face.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Change this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging configuration
logging.basicConfig(level=logging.INFO)

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
async def register(
    username: str = Form(...),
    file: UploadFile = None,
    db: SessionLocal = Depends(get_db),
):
    logging.info(f"Attempting to register user: {username}")
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")

    if db.query(User).filter(User.username == username).first():
        logging.error("Username already exists")
        raise HTTPException(status_code=400, detail="Username already exists")

    try:
        # Load image and extract face encoding
        image = face_recognition.load_image_file(file.file)
    except UnidentifiedImageError:
        logging.error("Invalid image format")
        raise HTTPException(status_code=400, detail="Invalid image format")

    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) != 1:
        logging.error(
            f"Face detection error for username: {username}, encodings found: {len(face_encodings)}"
        )
        raise HTTPException(
            status_code=400,
            detail="Face detection error: Ensure the image has a single, clear face",
        )

    face_encoding = face_encodings[0]
    new_user = User(username=username, face_encoding=pickle.dumps(face_encoding))
    db.add(new_user)
    db.commit()
    logging.info(f"User {username} registered successfully")
    return {"message": "New user added to database"}


# User login
@face.post("/login")
async def login(file: UploadFile = None, db: SessionLocal = Depends(get_db)):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")

    try:
        # Load image and extract face encoding
        image = face_recognition.load_image_file(file.file)
    except UnidentifiedImageError:
        logging.error("Invalid image format during login")
        raise HTTPException(status_code=400, detail="Invalid image format")

    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) != 1:
        logging.error(
            f"Face detection error during login, encodings found: {len(face_encodings)}"
        )
        raise HTTPException(
            status_code=400,
            detail="Face detection error: Ensure the image has a single, clear face",
        )

    face_encoding = face_encodings[0]
    users = db.query(User).all()

    for user in users:
        saved_encoding = pickle.loads(user.face_encoding)
        match = face_recognition.compare_faces([saved_encoding], face_encoding)

        if match[0]:
            logging.info(f"User {user.username} logged in successfully")
            return {"message": f"Hi, {user.username}! How are you?"}

    logging.error("Face does not match any user")
    raise HTTPException(status_code=400, detail="Face does not match any user")