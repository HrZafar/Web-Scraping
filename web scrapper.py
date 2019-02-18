import requests
from bs4 import BeautifulSoup

websites = {'URLs': ['https://tribune.com.pk/', 'https://www.dawn.com'],
            'attrs1': ['story', 'border-3'],
            'attrs2': ['story clearfix', 'template__header'],
            'desc': ['h1', 'h2']}

records = []

for i in range(len(websites['URLs'])):
    r = requests.get(websites['URLs'][i])
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('div', attrs={'class': websites['attrs1'][i]})

    if i == 1:
        results = results[0].find_all('article')
    url = str(results[0].find('a')['href'])

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('div', attrs={'class': websites['attrs2'][i]})

    website = websites['URLs'][i]
    link = url
    description = results[0].find(websites['desc'][i]).text.strip()
    if i == 0:
        date = results[0].find_all('div')[3].text.split()
        author = results[0].find_all('div')[2].text.split()
        author.pop(0)
        author = ' '.join(author)
    elif i == 1:
        date = results[0].find('div')('span')[2].text.split(' ')
        author = results[0].find('div')('span')[0].text
    date.pop(0)
    date = ' '.join(date)

    records.append(list((website, date, author, description, link)))

print(records[0])
print(records[1])
