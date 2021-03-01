import requests

Base = "http://127.0.0.1:5000/"

response = requests.patch(Base+ "video/2", {"likes": 100, "name": "hi there!!"})
print(response.json())
input()
response = requests.get(Base + "video/2")
print(response.json())
