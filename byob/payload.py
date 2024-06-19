import requests
import time

for i in range(1, 15):
    requests.get("http://ecoprove:3000")
    print("dumb")
    time.sleep(1)

print("finish")