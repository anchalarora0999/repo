# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 23:48:43 2018

@author: mangalam
"""

import urllib2
wiki="https://www.timeanddate.com/weather/india/ghaziabad/hourly"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

A=[]
B=[]
for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    cells2=row.findAll('th')
    if cells != []:
        A.append(cells2[0].text.strip())
        B.append(cells[1].text.strip().split()[0])
import pandas as pd
df=pd.DataFrame(A,columns=['Rank'])
df['gaziabaad']=B


import urllib2
wiki="https://www.timeanddate.com/weather/@1258076/hourly"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

A=[]
B=[]
for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    cells2=row.findAll('th')
    if cells != []:
        A.append(cells2[0].text.strip())
        B.append(cells[1].text.strip().split()[0])
        
import pandas as pd
df["rohtak"]=B



import urllib2
wiki="https://www.timeanddate.com/weather/@1255744/hourly"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

A=[]
B=[]
for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    cells2=row.findAll('th')
    if cells != []:
        A.append(cells2[0].text.strip())
        B.append(cells[1].text.strip().split()[0])
        
import pandas as pd
df["sonipat"]=B


import urllib2
wiki="https://www.timeanddate.com/weather/@1255744/hourly"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

A=[]
B=[]
for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    cells2=row.findAll('th')
    if cells != []:
        A.append(cells2[0].text.strip())
        B.append(cells[1].text.strip().split()[0])
        
import pandas as pd
df["meerut"]=B


import urllib2
wiki="https://www.timeanddate.com/weather/@7279746/hourly"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

A=[]
B=[]
for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    cells2=row.findAll('th')
    if cells != []:
        A.append(cells2[0].text.strip())
        B.append(cells[1].text.strip().split()[0])
        
import pandas as pd
df["noida"]=B

import urllib2
wiki="https://www.timeanddate.com/weather/india/new-delhi/hourly"
page= urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup =BeautifulSoup(page)

right_table=soup.find_all('table',class_="zebra")

right_table_tbody = right_table[0].findAll('tbody')

A=[]
B=[]
for row in right_table_tbody[0].findAll('tr'):
    cells=row.findAll('td')
    cells2=row.findAll('th')
    if cells != []:
        A.append(cells2[0].text.strip())
        B.append(cells[1].text.strip().split()[0])
        
import pandas as pd
df["delhi"]=B

features=df.iloc[:,1:-1].values
labels=df.iloc[:,-1].values
from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)

#model score
Score=regressor.score(features_test,labels_test)

from sklearn.model_selection import cross_val_score
accuracy=cross_val_score(estimator=regressor,X=features_train,y=labels_train,cv=10)
print"mean accuracy=",accuracy.mean()
print accuracy.std()


