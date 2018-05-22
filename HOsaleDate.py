#stuff we need for file and data
import os
import numpy as np
import pandas as pd
#stuff we need for zillow
import zillow

api = zillow.ValuationApi()

#The working file is on the Desktop
print(os.getcwd())
os.chdir("C:\\users\\"+os.getlogin()+"\\Desktop")
print(os.getcwd())

with open("zillow_key.txt", 'r') as f:
    key = f.readline().replace("\n", "")

df = pd.read_excel("HO Data 6-12 claims 2017.xlsx")

#Need to Index Data through Zillow and add to DataFrame, this works for a single value
for x in range(0, 1):  #replace number with df.shape[0] for full ist
    try:
        address = df.iloc[x,7] #+ ", " + df.iloc[x,8] + ", " + df.iloc[x,9] Commented out City and State
        postal_code = np.int(df.iloc[x,11]) #numbers come out as float64 and need to be converted for Zillow's API
        print(address)
        print(postal_code)
        data = api.GetDeepSearchResults(key,address,postal_code)
        print(data.extended_data.last_sold_date)
        df.iloc[x,13] = data.extended_data.last_sold_date
    except Exception as e:
        es = str(e)
        target = "</lastSoldDate>"
        if target in es:
            df.iloc[x,13] = es[es.find(target)-10:es.find(target)]
        else:
            df.iloc[x,13] = es
    x += 1

# This works for writing back to Excel
writer = pd.ExcelWriter('file.xlsx')
df.to_excel(writer,'Output')
writer.save()