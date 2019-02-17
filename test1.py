import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.dawn.com')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'border-3'})
results = results[0].find_all('article')
url = str(results[0].find('a')['href'])

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'template__header'})

website = 'https://www.dawn.com'
description = results[0].find('h2').text
date = results[0].find('div')('span')[2].text.split(' ')
date.pop(0)
date = ' '.join(date)
author = results[0].find('div')('span')[0].text
link = url

record = []
record.append(list((website, date, author, description, link)))
print(record)
