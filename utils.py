import requests
from bs4 import BeautifulSoup


def findSite(url):
	
	response = requests.get(url)
	html = response.content

	return BeautifulSoup(html, "html.parser")

def getSecondURL(name): 
	url = "https://www.sports-reference.com/cbb/players/"
	urlName = name.replace(" ", "-")
	urlName = urlName.replace("'", "")
	url += urlName + "-1.html"
	return findSite(url)