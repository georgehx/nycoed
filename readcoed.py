# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:22:46 2019

@author: 44100521
"""


import pandas as pd
from lxml import html
from bs4 import BeautifulSoup


def cleanTable(df):
   return df.loc[(df['Pts']!=0)&(df['L']!=0)]

with open('html.out', 'r') as myfile:
  data = myfile.read().replace('\n', '')

dfs = pd.read_html(data)

soup = BeautifulSoup(data, "lxml")

df1 = cleanTable(dfs[0])

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


print(df1)
print(df2)


# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:22:46 2019

@author: 44100521
"""

"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

int = range(1, 6)
f1=open('./html.out', 'a')

def cleanTable(df):
   return df.loc[(df['Pts']!=0)&(df['L']!=0)]

boots = ['goals', 'player', 'team']

for i in int:
    s = 'https://www.nycoedsoccer.com/league/'+str(i)+'/schedule/'
    ret = requests.head(s,timeout=5)
    if ret.status_code == 200:
        ret = requests.get(s,timeout=5)
        data = ret.text
        dfs = pd.read_html(data)
        soup = BeautifulSoup(data, "lxml")

        df1 = cleanTable(dfs[0])

# BSoup way to find content between tags:
# credits = soup.find_all("div", {"class" : "scorer"})
# gols = soup.find_all("p", {"class" : "goals"})
# This returns a list of appearances: [<p class="goals">23</p>, <p class="goals">11</p>]
# gols[0].get_text() returns the value 23

        dict1={}

        for b in boots:
            values = soup.find_all("p", {"class" : b})
            lst = []
            for v in values:
                lst.append(v.get_text())
                dict1[b] = lst

        df2 = pd.DataFrame(dict1)

        if i == 4:
            dfTable = df1
            dfBoot = df2
        else:
            dfTable = dfTable.append(df1)
            dfBoot = dfBoot.append(df2)

        print(dfs)


f1.close()

#dfTable.to_csv('table.csv')
print('Completed!')

"""


# # Below is to get HTML for that webpage

# int = 130 #range(130, 131)
# #f1=open('./b.out', 'a')
# #for i in int:
# s = 'https://www.nycoedsoccer.com/league/'+str(int)+'/schedule/'
# #s = 'http://nycoedsoccer.com'
# ret = requests.get(s,timeout=5)
# print(ret.text)
# ret.close()
