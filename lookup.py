from utils import *

def main(): 
	while True:
		while True:
			query = "bkref cbb "
			test = input("BKREF Search: ").strip()
			query += test
			url = searchGoogle(query)
	
			soup = findSite(url)
			div = soup.find("div", {"class": "nothumb"})
			number = soup.find("text", {"fill":"#ffffff"})
				
			if not (div and number): #If the original google search failed, try more direct approach
				soup = getSecondURL(test)
				div = soup.find("div", {"class": "nothumb"})
				number = soup.find("text", {"fill":"#ffffff"})
			
			if not (div and number):
				print("Sorry, we cannot find that player. Please try again.")
				query = ""
				test = ""
			else:
				break;
		
		name = str(div).split("h1",2)[1]
		name = name[17:-2]
		print("")
		print(name)
		print("")
	
		height = str(div).split("span",2)[1]
		height = str(div).split("span",2)[1]
		height = height[19:-2]
		print("Height: ", height)
	
		weight = str(div).split("span",2)[2]
		weight = weight[27:32]
		print("Weight: ", weight)
	
		
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
		print("")
		print("")
		print("")
		exitPrompt = input("Enter q to quit or anything else to search again:").strip()
		if (exitPrompt == 'q'):
			break;

	
if __name__ == "__main__":
    main()




