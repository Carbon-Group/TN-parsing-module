import requests
from bs4 import BeautifulSoup

url = 'https://www.tn.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

text = ''
for string in soup.strings:
    if string.strip():
        text += string.strip() + '\n'

with open('tn_ru_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)