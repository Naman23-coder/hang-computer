import requests

pi = requests.get('https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt').text
while True:
   print(pi*24578855885588657875886)
