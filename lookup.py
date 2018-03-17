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
	div = age_soup.find("div", {"id": "nba_player_stats_middle"})
	if not div:
		return "N/A"
	else:
		getName = age_soup.find("h2", {"class":"number"})
		length = len(name)+5
		getName = str(getName)[-length:-5]
		if (name != str(getName)): #If the NBADraftNet result is incorrect
			return "N/A"
		else:
			return div

def getAge(info):
	birthday = str(info).split("</span>",2)[1]
	birthday = birthday[1:-43]
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
	table = content.find("table", {"id": "players_per_game"})
	stat_year = table("tr")[-2] #Guarantee most recent season
	#print(stat_year)
	FGp = stat_year.find("td", {"data-stat": "fg_pct"})
	FGp = (str(FGp))[38:-5]
	print("FG%: ", FGp)
	tFGp = stat_year.find("td", {"data-stat": "fg2_pct"})
	tFGp = (str(tFGp))[39:-5]
	print("2FG%: ", tFGp)
	thFGp = stat_year.find("td", {"data-stat": "fg3_pct"})
	thFGp = (str(thFGp))[39:-5]
	print("3FG%: ", thFGp)
	FTp = stat_year.find("td", {"data-stat": "ft_pct"})
	FTp = (str(FTp))[38:-5]
	print("FT%: ", FTp)

def printYearlyAverages(content):
	table = content.find("table", {"id": "players_per_game"})
	stat_year = table("tr")[-2] #Guarantee most recent season
	PPG = stat_year.find("td", {"data-stat": "pts_per_g"})
	PPG = (str(PPG))[41:-5]
	print("PPG: ", PPG)
	RPG = stat_year.find("td", {"data-stat": "trb_per_g"})
	RPG = (str(RPG))[41:-5]
	print("RPG: ", RPG)
	APG = stat_year.find("td", {"data-stat": "ast_per_g"})
	APG = (str(APG))[41:-5]
	print("APG: ", APG)
	SPG = stat_year.find("td", {"data-stat": "stl_per_g"})
	SPG = (str(SPG))[41:-5]
	print("SPG: ", SPG)
	BPG = stat_year.find("td", {"data-stat": "blk_per_g"})
	BPG = (str(BPG))[41:-5]
	print("BPG: ", BPG)



def printAdvancedNumbers(content): #FOR SOME REASON THE FIND DIV IS NOT WORKING SO I HAVE TO DO THIS STUPID WORKAROUND
	div = content.find("div", {"id": "all_players_advanced"})
	i1 = str(div).find("<tbody>")
	i2 = str(div).find("</tbody>")
	table = str(div)[i1:i2]
	stat_year = table.split("<tr")[-1]
	PER = stat_year.find("per")
	PERtxt = (str(stat_year))[PER+6:PER+10]
	print("PER: ", PERtxt)
	WS = stat_year.find("ws_per_40")
	WStxt = (str(stat_year))[WS+12:WS+16]
	print("WS/40: ", WStxt)
	BPM = stat_year.find("\"bpm\"")
	BPMtxt = (str(stat_year))[BPM+7:BPM+10]
	print("BPM: ", BPMtxt)
	#table = content.find("table", {"id": "players_per_poss"})
	#stat_year = table("tr")[-2] #Guarantee most recent season
	#ORTG = stat_year.find("td", {"data-stat": "off_rtg"})
	#ORTG = (str(ORTG))[41:-5]
	#print("ORTG: ", ORTG)
	#DRTG = stat_year.find("td", {"data-stat": "def_rtg"})
	#DRTG = (str(DRTG))[41:-5]
	#print("DRTG: ", DRTG)

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

number = soup.find("text", {"fill":"#ffffff"})
if (str(number)[24] == '9'):
	number = str(number)[34:-7]
else:
	number = str(number)[35:-7]
print("Number: ", number)

nbadraft_net_info = getNBADraftNetInfo(name)

if (nbadraft_net_info == "N/A"):
	print("Age:   N/A")
	print("Class: N/A")
else:
	age = getAge(nbadraft_net_info)
	print("Age: ", age)

	grade = getClass(nbadraft_net_info)
	print("Class: ", grade)

print("")
print(" ------- AVERAGES ---------")
printYearlyAverages(soup)
print("")
print(" ------- SHOOTING ---------")
printShootingNumbers(soup)
print("")
print(" ------- ADVANCED ---------")
printAdvancedNumbers(soup)




