import requests
import pandas as pd

r_url="http://httpbin.org/post"
request_result = requests.post(url=r_url,
                               json={"key":"UOP"})
print(request_result.status_code)
if request_result:
    print(request_result.json()['origin'])
else:
    print("Ivalid JSON file")

