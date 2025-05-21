import requests

r_url="https://www.google.com/search"
request_result = requests.get(url=r_url,
                              params={"q":"UOP"})
print(request_result.status_code)
print(request_result.url)
print(request_result.text)

