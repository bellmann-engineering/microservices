# docker build -t rest-api-image .
# docker run -p 5100:5100 rest-api-image:latest

FROM python:3.9.1-alpine3.12

RUN pip install flask

WORKDIR /app
COPY app.py .
RUN chmod u+x app.py
RUN chown xfs app.py

USER xfs 
CMD [ "python", "./app.py"]