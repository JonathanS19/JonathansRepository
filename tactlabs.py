import requests
from bs4 import BeautifulSoup

req = requests.get("https://toronto.craigslist.org/tor/apa/d/toronto-elegant-bedroom-den-with/7518775856.html")

soup = BeautifulSoup(req.content, "html.parser")

len(list(soup.span))

res1 = soup.find("span",class_="price")
res = soup.title

print("Title:")
print(res.get_text())
print("Price:")
print(res1.get_text())
