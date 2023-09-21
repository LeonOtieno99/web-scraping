import requests,bs4

res = requests.get('https://www.wired.com/story/peak-newsletter-that-was-80-years-ago/')
print(res.status_code)
scrapFile = res.text

soup = bs4.BeautifulSoup(scrapFile,'html.parser')

#scrap titles
titles = soup.find_all('title')
for title in titles:
    print('Title:', title.text)
 
#scrap links
for link in soup.find_all('a'):
    print('Link:',link.get('href'))

#scrap time of production
dates = soup.find_all('time')
for date in dates:
    print('Date',date.get('datetime')) 

