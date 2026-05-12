FROM python:3.12 
WORKDIR /app
COPY print.py .
ENTRYPOINT ["python3"]
CMD ["main.py"]