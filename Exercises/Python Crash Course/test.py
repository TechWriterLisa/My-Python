import requests

url = "https://api.openweathermap.org/data/2.5/weather?zip=95050&units=imperial&appid=58654466206badc3e5327616988bb48c"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)