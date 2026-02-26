import requests
from bs4 import BeautifulSoup 

# =========================================================
# using requests to "get" a webpage
url = 'https://search.books.com.tw/'
url += 'search/query/cat/all/key/python/sort/1/page/1/v/0/'

r = requests.get(url)

print(r.status_code) # 200

if r.status_code == requests.codes.ok: # OK!
  print("OK!")

# take a look at the HTML source code of the webpage
print(r.text) 
# =========================================================




# =========================================================
# using BeautifulSoup to parse the HTML source code: Part 1
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify()) # try it

# take a look at the page title
title_tag = soup.title
print(title_tag) 
print(title_tag.string)

# find all the <a> tags
a_tags = soup.find_all('a')
for tag in a_tags:
  print(tag)
  print("======")

# using the get_text() method
a_tags = soup.find_all('a')
for tag in a_tags:
  print(tag.get_text())
  print("======")

# focusing on a certain attribute
attr = {"class": "price"}
price_tags = soup.find_all("span", attrs = attr)
for tag in price_tags:
  print(tag)
  print("======")

# using the get_text() and strip() methods
attr = {"class": "price"}
price_tags = soup.find_all("span", attrs = attr)
for tag in price_tags:
  print(tag.get_text().strip())
  print("======")

# obtaining the prices by writing our own codes
attr = {"class": "price"}
price_tags = soup.find_all("span", attrs = attr)
prices = []

for tag in price_tags:
  t = tag.get_text().strip()
  index_comma = t.find(",")
  index_dollar = t.find("元")
    
  if index_comma >= 0:
    price_str = t[index_comma + 2:index_dollar - 1]
  else: 
    index_colon = t.find(":")
    price_str = t[index_colon + 2:index_dollar - 1]
  
  prices.append(int(price_str))

prices = prices[0:20]

# printing out the average price
print("Average price:", sum(prices) / len(prices))
# =========================================================




# =========================================================
# using BeautifulSoup to parse the HTML source code: Part 2

# obtaining the URLs of the products
attr = {"rel": "mid_name"}
title_tags = soup.find_all("a", attrs = attr)

titles = []
links = []

for tag in title_tags:
  # print(tag) # try it by yourself
  title_str = tag.get_text().strip()
  print(title_str)
  link_str = "https:" + tag["href"]
  print(link_str)
  titles.append(title_str)
  links.append(link_str)
  print("===")
# =========================================================

# =========================================================
# saving what we have into a CSV file
fn2 = "books.csv"
fh2 = open(fn2, "w", encoding = 'utf-8') # try "cp950" as encoding

for i in range(len(prices)):
  fh2.write(titles[i] + "," + str(prices[i]) + "," + links[i] + "\n")
fh2.close()
# =========================================================
