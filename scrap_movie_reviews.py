#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup

import requests



user_ids = []
user_ratings = []
user_reviews = []

movie_reviews ={}
movie_ratings = {}
movie_titles= {}

request_str = "http://www.imdb.com/title/tt1386697/reviews?start=0"
r  = requests.get(request_str)#"http://www.imdb.com/title/tt1386697/reviews-index?start=0")
#Just scores: http://www.imdb.com/title/tt1386697/reviews-index?start=0;count=1000
#Full reviews: #http://www.imdb.com/title/tt1386697/reviews?count=1000&start=0
data = r.text
#myF = open('hi.txt', 'wb')
#myF.write(data)
#print data

soup = BeautifulSoup(data)

title_link = soup.find('link')
title = title_link['href']
movie_id = title[26:35]

tr = soup.find("a", href="/title/" + str(movie_id) +"/")# tt1386697/")
movie_titles[movie_id] = tr.string

#<link rel="canonical" href="http://www.imdb.com/title/tt1386697/reviews" /><meta property="og:url" content="http://www.imdb.com/title/tt1386697/reviews" />
# print len(list_obj)

#movie_ratings['user'] = [(movie_id, rating)]
#movie_review['user'] = [(movie_id, review)]
list_obj = soup.find_all('img',attrs={"width":"102","height":"12"})
start = 0
while len(list_obj):
    try:
        for link in list_obj:
            # num_rating =  link['alt']
            rating = str(link['alt'])
            #print rating
            user_ratings.append(rating)
            # value = int(rating[0])/int(rating[2])
            # rating = float(float(num_rating[0])/float(10))
            user_obj = link.next.next.next.next.next.next
            text = link.next.next.next.next.next.next.next.next.next.next.next
            user_id = user_obj['href']
            #print user_id
            user_ids.append(user_id)
            # print user_id[8:len(user_id)-1]+","+title+","+str(rating)
            y = link.find_next("p") 
            try:
                if "*** This review may contain spoilers ***" in y.string:
                    y = y.find_next("p")
            #print ('66666')
            except:
                pass
            stri = str(y)
            stri = stri.replace("<br/>", "\n")
            stri = stri.replace("<p>", "Start: ")
            review = stri.replace("</p>", ":End ")
            user_reviews.append(review)
            #print review
            #print ('5555555')
            if user_id in movie_ratings:
                movie_ratings[user_id].append((movie_id, rating))
                movie_reviews[user_id].append((movie_id, review))
            else:
                movie_ratings[user_id] = [(movie_id, rating)]
                movie_reviews[user_id] = [(movie_id, review)]
        #print start
    except:
        print "errorrrrrrrrrrr"
         # index=index+1
        pass
    start +=len(list_obj)
    request_str = "http://www.imdb.com/title/tt1386697/reviews?start=" + str(start)
    print (request_str)
    r  = requests.get(request_str)#"http://www.imdb.com/title/tt1386697/reviews-index?start=0")
    data = r.text
    soup = BeautifulSoup(data)
    list_obj = soup.find_all('img',attrs={"width":"102","height":"12"})  
    print (len(list_obj))  
else:
    print "empty"


print ("Total reviews: ", start)
# try:
#     for link in soup.find_all('td'):
#          if  link.get('class')[0]== 'titleColumn':
# 		 # for child in link.descendants:
#   		 	# print child.string
# 		# print link.a.has_attr('href') 
# 		 for item in link.find_all('span',attrs={'class':'secondaryInfo'}):
# 			if item is not None:
# 				print item.next_element   
# 		 #a=link.find('a')
#                  #name=a.get_text()
#                  #temp=link.next_sibling
#                  #rating=temp.next_sibling.strong.text
#                  #temp2=link.span.next_sibling.next_sibling.next_sibling.next_sibling   
#                  #year=temp2.text    
#                  #print name+","+rating+","+year
        
# except:
#     pass