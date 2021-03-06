# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
import scipy as sp
from datetime import datetime

file="F:\\temp\\trip\\AK.csv"


headers = ['restaurant'] 
adress_labels = ['streetAddress', 'addressLocality', 'addressRegion_State', 'postalCode','Country']
review_labels = ['author','ratingValue','datePublished','ratingValue_2','reviewBody','ratingValue_3']
headers = headers + adress_labels + review_labels

data = pd.read_csv(file, sep=",",header=None)
data.columns = headers

#data.__getitem__('restaurant').__setitem__(0, str(data['restaurant'][0]).upper())

for i in range(0,len(data)):
    print(i)
    for j,header in enumerate(headers):
        if (str(data[header][i]).upper() == "NAN"):
            data.set_value(i,header,"")
        else:
            if (header == 'datePublished'):
                dt = datetime.strptime(str(data[header][i]).upper(), '%B %d, %Y')
                newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year) 
                data.set_value(i,header,newdate)
            else:
                data.set_value(i,header,str(data[header][i]).upper())
        #data.__getitem__(header).__setitem__(i, str(data[header][0]).upper())
        #data[header][i] = str(data[header][i]).upper()


### ohio
file='F:\\temp\\sac\\scratch\\ohio-b_random_selected_10000.csv'
data = pd.read_csv(file, sep=",")
for i in range(0,len(data)):
    for j,header in enumerate(data.columns):
        if (str(data[header][i]) == "nan"):
            data.set_value(i,header,"")
        else:
            if ((header == 'birth_date') or (header == 'register_date')):
                dt = datetime.strptime(str(data[header][i]), '%Y-%m-%d')
                newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year) 
                data.set_value(i,header,newdate)

## ncvoters
file='F:\\temp\\sac\\scratch\\ncvoter-a_random_selected_10000.csv'
data = pd.read_csv(file, sep=",")
data['mail_zipcode'] = data['mail_zipcode'].map('{:.0f}'.format)

for i in range(0,len(data)):
    for j,header in enumerate(data.columns):
        if (str(data[header][i]) == "nan"):
            data.set_value(i,header,"")
        else:
            if (header == 'registr_dt'):
                dt = datetime.strptime(str(data[header][i]), '%m/%d/%Y')
                newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year) 
                data.set_value(i,header,newdate)



data.to_csv('F:\\temp\\apagar.csv',index=False,encoding='utf-8',quoting=csv.QUOTE_ALL)
z = pd.read_csv('F:\\temp\\apagar.csv',sep=",").replace(np.nan, '', regex=True)

#I = pd.Index(a.columns_names, name="rows")
    
#ll = 12
#C = pd.Index(headers, name="columns")
#with codecs.open(file, mode='r', encoding='utf8') as f:
#    reader = csv.reader(f,delimiter=",",quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
#
#    pread = list(reader)
#    pdata = pd.DataFrame(index=range(0,len(pread)),columns=headers)
#    
#    index = 0
#    for row in pread:
#        if(ll != len(row)):
#            print("lascou")
#        nr = []
#        for i,att_name in enumerate(headers):
#            # date
#            if i == 8:
#                pass
#            else:
#                print("::" + att_name)
#                pdata[att_name][index] = "xXx"
#                #pdata[att_name][index] = row[i].upper()
        
#        nrdata.append(nr)
#        data.append(row)    
#        index += 1
#0 name
#1 address
#6 author
#7 grade
# 8 (date),9 (skip) ,10 (review) 
        
#        nr = []
#        for att in row:
#            att.
#linha = data[0]

from datetime import datetime
datestring = 'August 17, 2016'
dt = datetime.strptime(datestring, '%B %d, %Y')
print(dt.year, dt.month, dt.day)
#data = readQuoted(file,delimiter = ',')