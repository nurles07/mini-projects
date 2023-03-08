import json
import requests
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://samsungstore.kg/ru/'


response = requests.get(BASE_URL)

image_url = 'https://samsungstore.kg/cache/files/12238.jpg_w630_h480_resize.jpg?t=1669799256'

response = requests.get(image_url)

with open("images/test.jpg", "wb") as file:
    file.write(response.content)