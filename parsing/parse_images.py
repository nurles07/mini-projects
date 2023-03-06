import requests, json

image_url = ''
response = requests.get(image_url)

with open("test.jpg", "wb") as file:
    file.write(response.content)