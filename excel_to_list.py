import json
import os
import pandas
import numpy

print(os.getcwd())
os.chdir("C:\\users\\"+os.getlogin()+"\\Desktop")
print(os.getcwd())

df = pandas.read_excel("second_owner.xlsx")
list_to_store = []

for x in range(0, df.shape[0]):
    print(df.loc[x, "Claim #"])
    list_to_store.append(df.loc[x,"Claim #"])

f = open("checked_claims.txt", "w")
json.dump(list_to_store,f)
f.close

print(len(list_to_store))