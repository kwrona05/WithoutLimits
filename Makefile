install-frontend:
	npm install
	npm install react-router-dom
	npm install react-webcam
	npm install sass

install-backend:
	pip install sqlalchemy
	pip install fastapi
	pip install opencv
	pip install face-recognition
	pip install numpy
	pip install pydantic
	
install: install-frontend install-backend
run-backend:
	cd backend && uvicorn register:face --reload --port 3000

run-frontend:
	npm run dev

run: run-backend run-frontend
