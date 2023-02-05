# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:07:36 2021

@author: Robert
"""
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
html=requests.get("https://pleagueofficial.com/stat-player/2021-22/6#record")
html.encoding="utf-8"
soup=BeautifulSoup(html.text,"lxml")
a=soup.find("table",{"class":"table table-hover table-striped"})
b=a.tbody.find_all("tr")
Threea_a=2.704090909090909
Play = 19.789473684210527
Three={}
Name=[]
THree=[]
for row in b:
    play=int(row.find_all("td")[2].text)
    three_a=float(row.find_all("td")[8].text)
    if play >= Play and three_a>=Threea_a:
        name=row.find("th").text
        three=row.find_all("td")[9].text
        three=float(three.replace("%",""))/100
        three=round(three,2)
        Three[name]=three
Three=sorted(Three.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
for i in range(len(Three)):
    if i<=9:
        Name.append(Three[i][0]+"\n"+str(Three[i][1]))
        THree.append(Three[i][1])
plt.bar(Name,THree,label="3P%",color="purple",width=0.3,linewidth="2",edgecolor="black")
plt.legend()
plt.title("3P% of p league+'s player")
plt.ylabel("3P%")
plt.show()
        