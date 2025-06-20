# api-blog
A demo blog to experiment with building an application that interacts with a back-end using REST

# Launch the backend

cd backend  
uv sync  
source .venv/bin/activate  
cd app  
./manage.py migrate  
./manage.py runserver 0.0.0.0:8000  