#! /usr/bin/python3
from selenium import webdriver
import time

browser=webdriver.Chrome()


browser.get('https://www.fanspole.com/series/indian-t20-2018/players')

elem = browser.find_element_by_css_selector('#player_filter_form_js > input:nth-child(8)')

elem.click()

time.sleep(15)

playerList=[]
pointList=[]

i=1
while i:
	str1='#player_index_table > tbody > tr:nth-child('
	str1=str1+str(i)
	str1=str1+') > td.padt10.padb5.padl10 > a'
	str2='#player_index_table > tbody > tr:nth-child('
	str2=str2+str(i)
	str2=str2+') > td:nth-child(8)'
	elem = browser.find_elements_by_css_selector(str1)
	if len(elem)==0:
		break
	elem2= browser.find_elements_by_css_selector(str2)
	playerList.append(elem[0].text)
	pointList.append(elem2[0].text)
	i=i+1

i=0

while i<len(playerList):
	print(playerList[i]+" "+pointList[i])
	i=i+1

print(len(playerList))

