import requests
from bs4 import BeautifulSoup

r = requests.get('https://tribune.com.pk/')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'story'})
url = str(results[0].find('a')['href'])

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'story clearfix'})

website = 'https://tribune.com.pk/'
description = results[0].find('h1').text
link = url
author = results[0].find_all('div')[2].text.split()
author.pop(0)
author = ' '.join(author)
date = results[0].find_all('div')[3].text.split()
date.pop(0)
date = ' '.join(date)

record = []
record.append(list((website, date, author, description, link)))
print(record)
