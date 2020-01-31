# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:22:46 2019

@author: 44100521
"""
import requests
import os
os.chdir('C:\Z Drive\Python Folder\WebScrapping')



int = range(1, 2000)
f1=open('b1.out', 'a')
for i in int:
    s = 'https://www.nycoedsoccer.com/league/'+str(i)+'/schedule/'
    ret = requests.head(s,timeout=5)

    #f1.write(str(ret.status_code)+','+str(i)+'\n')

    print(i, ret.status_code, file=f1)

f1.close()
print('Completed!')




# # Below is to get HTML for that webpage

# int = 130 #range(130, 131)
# #f1=open('./b.out', 'a')
# #for i in int:
# s = 'https://www.nycoedsoccer.com/league/'+str(int)+'/schedule/'
# #s = 'http://nycoedsoccer.com'
# ret = requests.get(s,timeout=5)
# print(ret.text)
# ret.close()
