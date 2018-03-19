import lookup

def getSecondURL(name): 
	url = "https://www.sports-reference.com/cbb/players/"
	urlName = name.replace(" ", "-")
	urlName = urlName.replace("'", "")
	url += urlName + "-1.html"
	return findSite(url)