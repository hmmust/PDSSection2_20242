import requests

#r_url="https://www.google.com"
r_url="https://www.uop.edu.jo"
request_result = requests.get(url=r_url)
print(request_result.status_code)
print(request_result.url)
print(request_result.text)

