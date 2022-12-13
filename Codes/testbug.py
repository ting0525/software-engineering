import requests


def req_get(idtext , score):
    res = requests.get('http://localhost:80/api/add_message/1234', json={"id":idtext , "score":score})
    if res.ok:
        print(res.json())
        
idtext = "bug1"
score = 87
req_get(idtext , score)