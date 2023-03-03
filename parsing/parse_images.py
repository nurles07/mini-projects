import requests, json

image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJ6HjXpNIt5wMhlmyUedtsojU2NaunF-CkMQ&usqp=CAU'

response = requests.get(image_url)

with open("test.jpg", "wb") as file:
    file.write(response.content)