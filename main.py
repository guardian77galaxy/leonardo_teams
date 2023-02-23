import requests

response = requests.get("https://yotube.com/")

print(response.text)
