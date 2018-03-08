import requests
from bs4 import BeautifulSoup
from googlesearch import search
from datetime import *
from dateutil.relativedelta import *
import calendar

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
		grade = grade[8:13]
	return grade
	
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

