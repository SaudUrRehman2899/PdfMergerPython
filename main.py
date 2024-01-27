# importing requests
import requests
# Importing json to utilize it
import json
# creating a variable and asking a name of city via input function
city = input("Enter the Name of City : ")
# creating url using my api key which i requested via login on weatherapi.com
# adding city in url to give user more chance
url = f"http://api.weatherapi.com/v1/current.json?key=d9b5d1a293fb4602b48115356242401&q={city}&aqi=yes"
# creating a variable to utulize method of requests to load url

r = requests.get(url)
# print(r.text)
# creating a dictionary by utilizing json to differnciate between values
wdic = json.loads(r.text)
# Printing final output
print(wdic["current"]["temp_c"])# Portfolio
