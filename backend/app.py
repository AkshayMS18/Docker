print("Hello, microdegree")


# FROM nginx:latest
# WORKDIR /app
# RUN apt update && apt install -y nginx
# COPY main.py .
# ENV NAME=microdegree
# ENV JAVA-HOME=/usr/lib/jvm/java-11-openjdk-amd64 
# # EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

# FROM python:3.12 
# WORKDIR /app
# COPY print.py .
# ENTRYPOINT ["python3"]
# CMD ["print.py"]
