import requests
import time

NUMBER_REQUESTS = 2000
URL = "http://ngnix/metrics"

for i in range(1, NUMBER_REQUESTS):
    requests.get(url=URL)
    time.sleep(1)