import requests
from bs4 import BeautifulSoup

def getURL():
	return 'https://www.sports-reference.com/cbb/players/muhammad-ali-abdur-rahkman-1.html'

# name = input("BKREF Search: ")
# print(name)
url = getURL()
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
div = soup.find("div", {"class": "nothumb"})
name = str(div).split("h1",2)[1]
name = name[17:-2]
print(name)

