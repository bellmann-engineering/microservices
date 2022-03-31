docker build -t rest-api-image .
docker run -p 5100:5100 rest-api-image:latest
