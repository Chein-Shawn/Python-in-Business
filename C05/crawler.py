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
print(soup.prettiify())

# print(requests.codes.ok)
if r.status_code == requests.codes.ok: # OK!
  print("OK!")
  
# print(r.text)