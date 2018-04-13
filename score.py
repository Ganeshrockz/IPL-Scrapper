#! /usr/bin/python3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import subprocess
import time

fp = open('FinalPlayers.txt', mode='r', encoding='utf-8-sig')

players=fp.read()

fp.close()

it=0


fp2 = open('players.txt', mode='r', encoding='utf-8-sig')

totalList = str(fp2.read())

fp2.close()

nameList=["Anirudh.txt","chennaisuperkannis.txt","PPT.txt","TVM.txt","VVD.txt","CCC.txt","JM.txt","PZC.txt","VM.txt"]


pointList=["Anirudh.txt","chennaisuperkannis.txt","PPT.txt","TVM.txt","VVD.txt","CCC.txt","JM.txt","PZC.txt","VM.txt"]

teamName=["Anirudh","ChennaiSuperKannis","PPT","TVM","VVD","CCC","JM","PZC","VM"]

fp3= open('Leaderboard.txt', mode='w', encoding='utf-8-sig')



while(it<len(nameList)):


	individualPlayerList=[]

	individualPointsList=[]

	fileName='Teams/'+str(nameList[it]);

	fp=open(fileName,mode='r', encoding='utf-8-sig')

	content=fp.read()

	fp.close()

	fileName='Points/'+str(pointList[it]);

	fp=open(fileName,mode='w', encoding='utf-8-sig')
	
	points=content.split(",")
	j=0
	total=0
	while(j<len(points)):
		points[j]=points[j].replace('\n','')
		points[j]=points[j].replace(' ','')
		pos=players.find(points[j])
		k=pos
		flag=0
		individualPlayer=""
		while(1):
			if(players[k]=='\n'):
				break
			if(players[k]==' ' and flag==0):
				flag=1
				k=k+1
				continue
			if(flag==1):
				individualPlayer=individualPlayer+players[k]
			k=k+1		
		#print(individualPlayer)
		count=0
		pos=totalList.find(str(individualPlayer))
		k=pos
		flag=0
		individualPoints=0
		minus=0
		space=0
		while(1):
			if(totalList[k]=='\n'):
				break
			if(totalList[k]==' '):
				space+=1
			k=k+1
		k=pos
		while(1):
			if(totalList[k]=='\n'):
				break
			if(totalList[k]==' '):
				count+=1
				if(count==space):
					flag=1
				k=k+1
				continue
			if(flag==1):
				if(totalList[k]=='-'):
					minus=1
				else:
					individualPoints=individualPoints*10+int(totalList[k])
			k=k+1
		if(minus==1):
			individualPoints=-individualPoints	
		individualPlayerList.append(individualPlayer)
		individualPointsList.append(individualPoints)
		total=total+individualPoints
		j=j+1

	i=0

	while(i<len(individualPointsList)):
		ans=individualPlayerList[i]+" "+str(individualPointsList[i])
		fp.write(ans)
		fp.write('\n')
		i=i+1

	fp.close()

	ans1=teamName[it]+" "+str(total)
	
	fp3.write(ans1)
	fp3.write('\n')
	it=it+1

fp3.close()

subprocess.call(["echo","\n"])
subprocess.call(["sort","-k2","-n","-r","Leaderboard.txt"])
subprocess.call(["echo","\n"])