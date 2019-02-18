import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.dawn.com')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'border-3'})
results = results[0].find_all('article')

records = []
for i in range(len(results)):
    url = str(results[i].find('a')['href'])

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find_all('div', attrs={'class': 'template__header'})

    website = 'https://www.dawn.com'
    description = results[i].find('h2').text.strip()
    date = result[0].find('div')('span')[2].text.split(' ')
    date.pop(0)
    date = ' '.join(date)
    author = result[0].find('div')('span')[0].text
    link = url
    records.append(list((website, date, author, description, link)))

for i in range(len(records)):
    print(records[i])
