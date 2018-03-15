import requests
from bs4 import BeautifulSoup
from googlesearch import search
from datetime import *
from dateutil.relativedelta import *
import calendar

def findSite(url):
	
	response = requests.get(url)
	html = response.content

	return BeautifulSoup(html, "html.parser")

def getNBADraftNetInfo(name):
	age_query = "nbadraft net " + name
	for j in search(age_query, num=1, stop=1):
		age_url = j
	
	age_response = requests.get(age_url)
	age_html = age_response.content

	age_soup = BeautifulSoup(age_html, "html.parser")
	return age_soup.find("div", {"id": "nba_player_stats_middle"})
	
def getAge(info):
	birthday = str(info).split("</span>",2)[1]
	birthday = birthday[1:-43]
	print(birthday)
	birthdate = datetime.strptime(birthday, '%m/%d/%y').strftime('%Y-%m-%d')
	difference_in_years = relativedelta(date.today(), datetime.strptime(birthdate, '%Y-%m-%d')).years
	difference_in_months = relativedelta(date.today(), datetime.strptime(birthdate, '%Y-%m-%d')).months
	return round(difference_in_years + (difference_in_months/12), 2)

def getClass(info):
	grade = str(info).split("Class:",10)[1]
	if (grade[8] == 'F'):
		grade = grade[8:16]
	elif (grade[8] == 'S' and grade[9] == 'o'):
		grade = grade[8:17]
	else:
		grade = grade[8:14]
	return grade
	
def printShootingNumbers(content):
	div = content.find("table", {"id": "players_per_game"})
	FGp = div.find("td", {"data-stat": "fg_pct"})
	FGp = (str(FGp))[38:-5]
	print("FG%: ", FGp)
	tFGp = div.find("td", {"data-stat": "fg2_pct"})
	tFGp = (str(tFGp))[39:-5]
	print("2FG%: ", tFGp)
	thFGp = div.find("td", {"data-stat": "fg3_pct"})
	thFGp = (str(thFGp))[39:-5]
	print("3FG%: ", thFGp)
	FTp = div.find("td", {"data-stat": "ft_pct"})
	FTp = (str(FTp))[38:-5]
	print("FT%: ", FTp)
	
	
	
query = "bkref cbb "
test = input("BKREF Search: ")
query += test

for j in search(query, num=1, stop=1):
	url = j

soup = findSite(url)
div = soup.find("div", {"class": "nothumb"})
	
if not div: #If the original google search failed, try more direct approach
	url = "https://www.sports-reference.com/cbb/players/"
	urlName = test.replace(" ", "-")
	urlName = urlName.replace("'", "")
	url += urlName + "-1.html"
	print(url)
	soup = findSite(url)
	div = soup.find("div", {"class": "nothumb"})

name = str(div).split("h1",2)[1]
name = name[17:-2]
print("")
print(name)
print("")

height = str(div).split("span",2)[1]
height = height[19:-2]
print("Height: ", height)

weight = str(div).split("span",2)[2]
weight = weight[27:32]
print("Weight: ", weight)

nbadraft_net_info = getNBADraftNetInfo(name)

age = getAge(nbadraft_net_info)
print("Age: ", age)

grade = getClass(nbadraft_net_info)
print("Class: ", grade)

print("")
print(" ------- SHOOTING ---------")
printShootingNumbers(soup)




