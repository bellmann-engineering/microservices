1) von root Folder der Solution aus:
`docker build -t webappimage -f WebApp/Dockerfile .`

2) Start als Deamon / Port mapping beachten:
`docker run -d -p 8080:80 --name webappcontainer webappimage`

3) Prüfen:
`docker ps`

4) `curl -v http://localhost:8080/weatherforecast`

5) im Webbrowser: `http://localhost:8080/weatherforecast`
