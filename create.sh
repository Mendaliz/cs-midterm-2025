docker build -t flask-dev .
docker image ls | head -n 3
docker run -d -v "$(pwd)":/app -p 8080:8080 --name flask-dev-container flask-dev
docker container ls -a | head -n 3
echo "initializing server..."
sleep 2
python client.py