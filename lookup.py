import requests
from bs4 import BeautifulSoup
from googlesearch import search

def getURL():
	return 'https://www.sports-reference.com/cbb/players/muhammad-ali-abdur-rahkman-1.html'

query = "bkref cbb "
query += input("BKREF Search: ")
#print(query)

for j in search(query, num=1, stop=1):
	url = j

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
div = soup.find("div", {"class": "nothumb"})
name = str(div).split("h1",2)[1]
name = name[17:-2]
print(name)

