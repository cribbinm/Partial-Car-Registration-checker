#! python3

#Car reg checker

import sys, bs4, webbrowser, requests

year = input("Enter the year of the car. Example: 161, 99, etc.")
county = input("Enter the county code of the car. Example: D, KK, RN, etc.")
partialreg = input("Enter a partial car registration with X's for the unknown digits, example:161D2XXX5")
carmake = input("Enter the make of the car e.g. Volkswagen")
carcolour = input("Enter the colour of the car in all caps e.g. BLACK")


print('Downloading car reg..')
yearlist = list(year)
carreglist = list(partialreg)
countylist = list(county)
length = len(yearlist)+len(carreglist)+len(countylist)
partialdigits = carreglist.count(X)

def regcheck0(reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9):
	res = requests.get('http://www.mywheels.ie/free-car-check-report/?VRN='+str(reg0)+str(reg1)+str(reg2)+str(reg3)+str(reg4)+str(reg5)+str(reg6)+str(reg7)+str(reg8)+str(reg9)+'5')
	res.raise_for_status
	restext = res.text
	soup = bs4.BeautifulSoup(restext)
	return soup.select('.value')[0].getText(),soup.select('.value')[1].getText(),soup.select('.value')[2].getText(),soup.select('.value')[3].getText(),soup.select('.value')[4].getText(),soup.select('.value')[5].getText()

def regcheck9(reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9):
	res = requests.get('http://www.mywheels.ie/free-car-check-report/?VRN='+str(reg0)+str(reg1)+str(reg2)+str(reg3)+str(reg4)+str(reg5)+str(reg6)+str(reg7)+str(reg8)+str(reg9)+'5')
	res.raise_for_status
	restext = res.text
	soup = bs4.BeautifulSoup(restext)
	return soup.select('.value')[0].getText(),soup.select('.value')[1].getText(),soup.select('.value')[2].getText(),soup.select('.value')[3].getText(),soup.select('.value')[4].getText(),soup.select('.value')[5].getText()

def regcheck8(reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9):
	res = requests.get('http://www.mywheels.ie/free-car-check-report/?VRN='+str(reg0)+str(reg1)+str(reg2)+str(reg3)+str(reg4)+str(reg5)+str(reg6)+str(reg7)+str(reg8)+str(reg9)+'5')
	res.raise_for_status
	restext = res.text
	soup = bs4.BeautifulSoup(restext)
	return soup.select('.value')[0].getText(),soup.select('.value')[1].getText(),soup.select('.value')[2].getText(),soup.select('.value')[3].getText(),soup.select('.value')[4].getText(),soup.select('.value')[5].getText()

def regcheck7(reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9):
	res = requests.get('http://www.mywheels.ie/free-car-check-report/?VRN='+str(reg0)+str(reg1)+str(reg2)+str(reg3)+str(reg4)+str(reg5)+str(reg6)+str(reg7)+str(reg8)+str(reg9)+'5')
	res.raise_for_status
	restext = res.text
	soup = bs4.BeautifulSoup(restext)
	return soup.select('.value')[0].getText(),soup.select('.value')[1].getText(),soup.select('.value')[2].getText(),soup.select('.value')[3].getText(),soup.select('.value')[4].getText(),soup.select('.value')[5].getText()

def regcheck6(reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9):
	res = requests.get('http://www.mywheels.ie/free-car-check-report/?VRN='+str(reg0)+str(reg1)+str(reg2)+str(reg3)+str(reg4)+str(reg5)+str(reg6)+str(reg7)+str(reg8)+str(reg9)+'5')
	res.raise_for_status
	restext = res.text
	soup = bs4.BeautifulSoup(restext)
	return soup.select('.value')[0].getText(),soup.select('.value')[1].getText(),soup.select('.value')[2].getText(),soup.select('.value')[3].getText(),soup.select('.value')[4].getText(),soup.select('.value')[5].getText()

def regcheck5(reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9):
	res = requests.get('http://www.mywheels.ie/free-car-check-report/?VRN='+str(reg0)+str(reg1)+str(reg2)+str(reg3)+str(reg4)+str(reg5)+str(reg6)+str(reg7)+str(reg8)+str(reg9)+'5')
	res.raise_for_status
	restext = res.text
	soup = bs4.BeautifulSoup(restext)
	return soup.select('.value')[0].getText(),soup.select('.value')[1].getText(),soup.select('.value')[2].getText(),soup.select('.value')[3].getText(),soup.select('.value')[4].getText(),soup.select('.value')[5].getText()

def regcheck4(reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9):
	res = requests.get('http://www.mywheels.ie/free-car-check-report/?VRN='+str(reg0)+str(reg1)+str(reg2)+str(reg3)+str(reg4)+str(reg5)+str(reg6)+str(reg7)+str(reg8)+str(reg9)+'5')
	res.raise_for_status
	restext = res.text
	soup = bs4.BeautifulSoup(restext)
	return soup.select('.value')[0].getText(),soup.select('.value')[1].getText(),soup.select('.value')[2].getText(),soup.select('.value')[3].getText(),soup.select('.value')[4].getText(),soup.select('.value')[5].getText()


if length == 4:
	if len(yearlist)==2:
		if len(carreglist)==1:
			for i in range(999):
				try:
					car=regcheck(i)
					if car[1]=='BLACK':
					if car[2]=='Volkswagen':
					print car
				except IndexError: 
					continue	

	



for i in range(999):
	try:
		car=regcheck(i)
		if car[1]=='BLACK':
			if car[2]=='Volkswagen':
				print car
	except IndexError: 
		continue

