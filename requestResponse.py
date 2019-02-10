import json
import requests
import time
addr = "https://samples.openweathermap.org/data/2.5/weather?lat=123&lon=456&appid=b6907d289e10d714a6e88b30761fae22"
resp = requests.get(url=addr)
#print "Response:: ",resp.text
print ""

dataDict = json.loads(resp.text)
print "data[\"weather\"] :: ",dataDict["weather"][0]["main"]
