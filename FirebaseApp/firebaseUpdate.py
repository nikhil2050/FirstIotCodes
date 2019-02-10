import time
from firebase import firebase
fb = firebase.FirebaseApplication("https://firstiotproject-c401a.firebaseio.com/",None)
count = 0

while True:
	fb.put("/", "lat", count)
	fb.put("/", "lon", count+1)
	count = count+1
	time.sleep(3)
