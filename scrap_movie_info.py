
from bs4 import BeautifulSoup

import requests

imbbID = 'tt0108052'

r = requests.get("http://www.imdb.com/title/" + imdbID + "/")

list_obj = soup.find_all('span', itemprop="genre")
for list in list_obj:
	print str(list.string)

data = r.text  
soup = BeautifulSoup(data)

d_obj = soup.find('span', itemprop="director")
t = d_obj.find('a')

 #name = t.string
 #full_link = t['href']
 #name_id = te[6:15]

rat = soup.find('span', attrs={"class":"rating"})
rating = str(a.next.string)

d2_obj = d_obj.find_next("span", itemprop="director")
t2 = d2_obj.find('a')

#name = t2.string
#full_link = t2['href']
#name_id = te2[6:15]


w_obj = soup.find('span', itemprop="creator")
t = w_obj.find('a')

d2_obj = d_obj.find_next("span", itemprop="director")
 t2 = d2_obj.find('a')

act  = soup.find_all('td',attrs={ "itemprop":"actor"})
actr = act[:10]
links = []
names = []
for actor in actr:
	temp = actor.find('a')
	links.append(temp['href'])
	names.append(str(temp.find('span').string))


Coun = str(soup.find('h4', string = 'Country:').find_next('a').string)
Rdate = str(soup.find('h4', string = 'Release Date:').next.next.string).split('(')[0][1:-1]

Rdate = str(soup.find('h4', string = 'Gross:').string).split('(')[0][1:-1]
Gross = str(soup.find('h4', string = 'Gross:').next.next.string)[8:-16]
Color = str(soup.find('h4', string = 'Country:').find_next('a').string)

r = requests.get("http://www.imdb.com/title/" + imdbID + "/trivia?tab=mc&ref_=tt_trv_cnn")
data = r.text  
soup = BeautifulSoup(data)
Follow = []
b = soup.find('a',attrs = { "id":"follows"}).find_next('a')
NextAvail = True
while (NextAvail):
	Follow.append(b['href'])
	b = b.find_next('a')
	try:
		c = b['href']
	except:
		NextAvail = False


b = soup.find('a',attrs = { "id":"followed_by"}).find_next('a')
NextAvail = True
while (NextAvail):
	Follow.append(b['href'])
	b = b.find_next('a')
	try:
		c = b['href']
	except:
		NextAvail = False


