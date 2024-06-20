import requests
import time

# URL to attack
URL = "http://ecoprove-api-build-1/metrics"
print(f"Attacking ${URL}")

# basic loop for keep fething the server to try to overload it
while True:
    requests.get(url=URL)
    time.sleep(0.2)