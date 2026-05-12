FROM python:3.8-slim
WORKDIR /app
RUN apt update && apt install -y nginx
COPY app.py .
ARG SERVER_PORT=80
ENV SERVER_PORT=${SERVER_PORT}
EXPOSE ${SERVER_PORT}
CMD ["python3", "main.py"]

# FROM python:3.12 
# WORKDIR /app
# COPY print.py .
# ENTRYPOINT ["python3"]
# CMD ["print.py"]
