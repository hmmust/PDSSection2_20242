import requests
from pyquery import PyQuery as pq
url="https://www.kooora.com/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D9%85%D9%88%D8%A7%D8%B9%D9%8A%D8%AF-%D9%86%D8%AA%D8%A7%D8%A6%D8%AC/2025-05-20"
kooora = requests.get(url=url)
koora_doc = pq(kooora.text)
matches = pq(koora_doc('div.fco-match-row'))
print(matches.length)