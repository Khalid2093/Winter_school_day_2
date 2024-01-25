import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'height':172.00})

print(r.json())