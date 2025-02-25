FROM python:3
WORKDIR /app
COPY name.py /app/
CMD ["python", "/app/name.py"]
