import json

import requests
import numpy as np
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#from matplotlib.pyplot import figure

#calling from api
url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india_timeline"

headers = {
    "X-RapidAPI-Key": "3ce98f40cdmsh3c0fa1eaed93697p165265jsn26b44c6f51b5",
    "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
details= json.loads(response.text)

print(response.text)

# Create table of covid details  with daily confirmed, daily deceased, daily recovered, date, dateymd, total confirmed, total deceased and total recovered
covidDetails = []

# Adding information to a list
for stat in details:

    covidDetails.append([stat['dailyconfirmed'], stat['dailydeceased'], stat['dailyrecovered'], stat['date'], stat['dateymd'],
                     stat['totalconfirmed'], stat['totaldeceased'],stat['totalrecovered']])

# Use as numpy array
covidDetailsArray = np.array(covidDetails)

# Use as pandas dataframe
covidDF = pd.DataFrame(covidDetails, columns=['dailyConfirmed', 'dailyDeceased', 'dailyRecovered','date', 'dateymd', 'totalConfirmed',
                                              'totalDeceased','totalRecovered'])

covidDF.to_excel('data.xlsx', sheet_name='sheet1', index=False)