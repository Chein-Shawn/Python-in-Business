import requests
from bs4 import BeautifulSoup 

# =========================================================
# using requests to "get" a webpage
# url = 'https://search.books.com.tw/'
# url += 'search/query/cat/all/key/python/sort/1/page/1/v/0/'

url = 'http://quotes.toscrape.com/'

# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/120.0.0.0 Safari/537.36"
# }

# 抓取source code, 放進名為r的class
r = requests.get(url)
print(r.status_code) # 200: ok!

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
title_tag = soup.title
print(title_tag)
print(title_tag.string)

# class_ (underscore): the HTML class attribute
# find_all("標籤名稱", attrs={"屬性": "值"})
author_tags = soup.find_all("small", class_="author")
for tag in author_tags:
  print(tag.get_text())
  print(tag.get_text().strip())
  print('*****************')
# print(requests.codes.ok)
if r.status_code == requests.codes.ok: # OK!
  print("OK!")
  
sentences = soup.find_all("span", class_= "text")
for line in sentences:
   print(line.get_text().strip())
   print("##############")


quotes = soup.find_all("div", class_="quote")
for q in quotes:
    tags = [a.get_text(strip=True) for a in q.find_all("a", class_="tag")]
    print(tags)
    print("@@@@@@@@@@@@@@@@@@@@@")
   

# print(r.text)

a_tags = soup.find_all('a')
b_tags = soup.find_all('b')
for tag in a_tags:
  print(tag)
  print(tag.get_text())
  print("==========")
for tag in b_tags:
  print(tag)
  print(tag.get_text())
  print("==========")


#   <span class="text" itemprop="text">
#        “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
#       </span>