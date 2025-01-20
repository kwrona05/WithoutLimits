install-frontend:
	npm install

install-backend:
	echo "installing backend"
	
install: install-frontend install-backend
run:
	cd backend && uvicorn register:face --reload --port 3000

