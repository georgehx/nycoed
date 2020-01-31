# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:22:46 2019

@author: 44100521
"""


import pandas as pd
from bs4 import BeautifulSoup

import os
os.chdir('C:\Z Drive\Python Folder\WebScrapping')




def cleanTable(df):
   return df.loc[(df['Pts']!=0) | (df['L']!=0)]
   #return df

#def addLeague(leag):
#    lstLeague.append(leag)

def readData(file):
    with open(file, 'r') as myfile:
      data = myfile.read().replace('\n', '')
    
    dfs = pd.read_html(data)
    
    soup = BeautifulSoup(data, "lxml")
    
    leag = soup.body.find('div', attrs={'class':'col-md-12 col-xs-12 col-sm-12 league-cover'}).text
    #addLeague(leag)
    df1 = cleanTable(dfs[0])
    #df1 = dfs[0]
    if len(dfs) == 2:
        df3 = cleanTable(dfs[1])
        
        #df3 = dfs[1]
        df1 = df1.append(df3)
    # BS way to find content between tags:
    # credits = soup.find_all("div", {"class" : "scorer"}) 
    # gols = soup.find_all("p", {"class" : "goals"}) 
    # This returns a list of appearances: [<p class="goals">23</p>, <p class="goals">11</p>]
    # gols[0].get_text() returns the value 23
    
    boots = ['goals', 'player', 'team']
    dict1={}
    
    for b in boots:
        values = soup.find_all("p", {"class" : b})
        lst = []
        for v in values:
            lst.append(v.get_text())
            dict1[b] = lst
            
    df2 = pd.DataFrame(dict1)
    
    #dfTable = dfTable.append(df1)
    #dfBoot = dfBoot.append(df2)
    
    
    #print(df1)
    #print(df2)
    return [df1,df2,leag]
    
mypath = 'data'

"""
os.listdir() will get you everything that's in a directory - files and directories.
If you want just files, you could either filter this down using os.path:
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
or you could use os.walk() which will yield two lists for each directory it visits - splitting into files and dirs for you. If you only want the top directory you can just break the first time it yields

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
"""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

os.chdir(mypath)

dfTable = pd.DataFrame()
dfBoot = pd.DataFrame()
lstLeague = []

for f in onlyfiles:
    dfTable = dfTable.append(readData(f)[0])
    dfBoot = dfBoot.append(readData(f)[1])
    lstLeague.append(readData(f)[2])
    print(readData(f)[2])

dfLeague = pd.DataFrame(lstLeague)
print(dfLeague)

writer = pd.ExcelWriter('../nycoedData.xlsx', engine='xlsxwriter')
dfTable.to_excel(writer, sheet_name='Table', index=False)
dfBoot.to_excel(writer, sheet_name='Boot',index=False)
dfLeague.to_excel(writer, sheet_name='League',index=False)

worksheet1 = writer.sheets['Table']
worksheet1.set_column('A:A', 30)

worksheet2 = writer.sheets['Boot']
worksheet2.set_column('C:C', 30)
worksheet2.set_column('B:B', 30)

writer.save()
#print(dfTable.shape)
#print(dfBoot.shape)    
#print(onlyfiles)