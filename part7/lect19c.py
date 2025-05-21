import requests
import pandas as pd

r_url="https://raw.githubusercontent.com/hmmust/PDSSection2_20242/refs/heads/main/part5/students_cleaned.json"
request_result = requests.get(url=r_url)
print(request_result.status_code)
#if request_result.status_code==200:
if request_result:
    
    df= pd.DataFrame(request_result.json())
    print(df)
else:
    print("Ivalid JSON file")

