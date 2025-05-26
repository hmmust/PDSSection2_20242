import requests
import pandas as pd
from pyquery import PyQuery as pq
url="https://www.kooora.com/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D9%85%D9%88%D8%A7%D8%B9%D9%8A%D8%AF-%D9%86%D8%AA%D8%A7%D8%A6%D8%AC/2025-05-20"
kooora = requests.get(url=url)
koora_doc = pq(kooora.text)
#print(pq(koora_doc('h1.fco-page-header')).text())
matches = pq(koora_doc('div.fco-match-row'))
print(matches.length)
matches_scores = []
for match in matches:
    match = pq(match)("div.fco-match-team-and-score")
    match = pq(match)
    team_a = match("div.fco-match-team-and-score__team-a")
    team_a = pq(pq(team_a)("div.fco-match-team-with-crest"))
    team_a = pq(team_a("div.fco-long-name")).text()
    
    team_b = match("div.fco-match-team-and-score__team-b")
    team_b = pq(pq(team_b)("div.fco-match-team-with-crest"))
    team_b = pq(team_b("div.fco-long-name")).text()
    scores = pq(match("div.fco-match-score__container"))
    scores = pq(match("div.fco-match-score"))
    score_a= pq(scores[0]).text()
    score_b= pq(scores[1]).text()
    m= {"team_a_name":team_a,"team_a_score":score_a,
        "team_b_score":score_b,"team_b_name":team_b}
    matches_scores.append(m)
    #print(team_a,score_a,'-',score_b,team_b)

matches = pd.DataFrame(matches_scores)
print(matches)
    
