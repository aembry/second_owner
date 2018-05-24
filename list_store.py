import json
import os

print(os.getcwd())
os.chdir("C:\\users\\"+os.getlogin()+"\\Desktop")
print(os.getcwd())

list_to_write = ["spam", "eggs", "biscuts"]


f = open("test.txt","w")
json.dump(list_to_write,f)
f.close()

f= open("test.txt", "r")

list_to_read = json.load(f) 

list_to_read.append("chips")

print(list_to_read)
