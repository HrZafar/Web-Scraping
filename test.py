import requests
from bs4 import BeautifulSoup

r = requests.get('https://tribune.com.pk/')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'story'})

records = []
for i in range(5):
    url = str(results[i].find('a')['href'])

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find_all('div', attrs={'class': 'story clearfix'})

    website = 'https://tribune.com.pk/'
    description = result[0].find('h1').text.strip()
    link = url
    author = result[0].find_all('div')[2].text.split()
    author.pop(0)
    author = ' '.join(author)
    date = result[0].find_all('div')[3].text.split()
    date.pop(0)
    date = ' '.join(date)
    records.append(list((website, date, author, description, link)))

for i in range(len(records)):
    print(records[i])
