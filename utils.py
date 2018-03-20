import requests
from bs4 import BeautifulSoup
from googlesearch import search
from datetime import *
from dateutil.relativedelta import *

def searchGoogle(query):
	for j in search(query, num=1, stop=1):
			url = j
	return url;

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

def getNBADraftNetInfo(name):
	age_url = searchGoogle("nbadraft net " + name)
	age_soup = findSite(age_url)
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
	if (str(stat_year)[BPM+10].isdigit()):
		BPMtxt = (str(stat_year))[BPM+7:BPM+11]
	else:
		BPMtxt = (str(stat_year))[BPM+7:BPM+10]
	print("BPM: ", BPMtxt)
	div = content.find("div", {"id": "all_players_per_poss"})
	i1 = str(div).find("<tbody>")
	i2 = str(div).find("</tbody>")
	table = str(div)[i1:i2]
	stat_year = table.split("<tr")[-1]
	ORTG = stat_year.find("off_rtg")
	if (str(stat_year)[ORTG+14].isdigit()):
		ORTGtxt = (str(stat_year))[ORTG+10:ORTG+15]
	else:
		ORTGtxt = (str(stat_year))[ORTG+10:ORTG+14]
	print("ORTG: ", ORTGtxt)
	DRTG = stat_year.find("def_rtg")
	if (str(stat_year)[DRTG+14].isdigit()):
		DRTGtxt = (str(stat_year))[DRTG+10:DRTG+15]
	else:
		DRTGtxt = (str(stat_year))[DRTG+10:DRTG+14]
	print("DRTG: ", DRTGtxt)
	

