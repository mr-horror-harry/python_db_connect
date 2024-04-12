# Setup
python3 -m venv venv

# To run the entire app
sudo docker-compose up --build

# To monitor the backend
sudo docker logs -f app_backend

# To enter the frontend to give input
sudo docker exec -it app_frontend /bin/bash

python3 app.py