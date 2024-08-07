import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qUrl = 'https://books.toscrape.com/'

qHeader = {
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

qResp = rq.get(url=qUrl, headers= qHeader)

bSoup = BeautifulSoup(qResp.content, 'html.parser')

def removeNavigableString(value):
    return list(filter(lambda x: type(x) != NavigableString, value))

c = removeNavigableString(bSoup.ol.children)
x = (c[4].h3)
t1 = (x.a.attrs['title'])

c = removeNavigableString(bSoup.ol.children)
x1 = (c[5].h3)
t2 = (x1.a.attrs['title'])

c = removeNavigableString(bSoup.ol.children)
x2 = (c[6].h3)
t3 = (x2.a.attrs['title'])

c = removeNavigableString(bSoup.ol.children)
x3 = (c[7].h3)
t4 = (x3.a.attrs['title'])

print("2 row titles :")

print('Title 1 : ',t1)
print('Title 2 : ',t2)
print('Title 3 : ',t3)
print('Title 4: ', t4)

