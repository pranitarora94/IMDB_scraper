from bs4 import BeautifulSoup

import requests
imdbID = 'tt0109830'
r  = requests.get("http://www.imdb.com/title/" + imdbID + "/synopsis?ref_=ttpl_pl_syn")
data = r.text
soup = BeautifulSoup(data)
a = soup.find('div', id='swiki.2.1')
pl = str(a)

p = pl.split('<')

fin = []
for para in p:
	te = para.split('>')
	if(len(te)>1):
		fin.append(te)

synop = ''
for para in fin:
	if len(para[1]) > 2:
		synop += str(para[1])