import json

import requests

from bs4 import BeautifulSoup as BS

image_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fnature%2F&psig=AOvVaw2ynqy4NimSMAN45I0eGLrT&ust=1678031318200000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCNiwrPbPwv0CFQAAAAAdAAAAABAE'


response = requests.get(image_url)

with open("test.jpg", "wb") as file:
    file.write(response.content)