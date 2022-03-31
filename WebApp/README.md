von root Folder der Solution aus:
docker build -t webappimage -f WebApp/Dockerfile .

Start als Deamon / Port mapping beachten:
docker run -d -p 8080:80 --name webappcontainer webappimage

Prüfen:
docker ps

Curl:
curl -v http://localhost:8080/weatherforecast

Browser:
http://localhost:8080/weatherforecast