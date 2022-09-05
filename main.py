import pandas as pd
import datetime
import requests
import os

os.chdir(r"D:\Final_Projects\BirthdayWisher")

def sendEmail(number, msg):
    # print('+91' + str(number))
    resp = requests.post('https://textbelt.com/text', {
        'phone': '+91' + str(number),
        'message': msg,
        'key': 'Enter your API Key here'
        # Use key = 'textbelt' to access the free version of the API
    })
    print(resp.json())


if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")

    today = datetime.datetime.now().strftime("%d-%m")
    # print(today)
    presentYear = datetime.datetime.now().strftime("%Y")

    sentList = []
    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
    
        if today == bday and presentYear not in str(item['Year']):
            sendEmail(item['Mobile'], item['Message'] + ' to ' + item['Name'])
            sentList.append(index)
    
    if sentList:
        for i in sentList:
            yr = df.loc[i, 'Year']
            df.loc[i, 'Year'] = str(yr) + ',' + str(presentYear)

        df.to_excel('data.xlsx', index = False)
    
