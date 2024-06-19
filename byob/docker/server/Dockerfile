FROM python:3.11.9-bullseye

WORKDIR /app

COPY . .

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN pip install requests

ENTRYPOINT ["python", "http_server.py"]