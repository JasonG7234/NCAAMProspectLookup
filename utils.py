def getSecondURL(name): 
	url = "https://www.sports-reference.com/cbb/players/"
	urlName = test.replace(" ", "-")
	urlName = urlName.replace("'", "")
	url += urlName + "-1.html"
	return findSite(url)