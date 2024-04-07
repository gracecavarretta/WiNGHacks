import http.client, urllib

inFile = open("myFile.txt", 'r')
option = inFile.readline()
inFile.close()

if option == "Hungry":
    message = "CrySense Notification: Your baby is hungry!"
elif option == "Uncomfortable":
    message = "CrySense Notification: Your baby is uncomfortable!"

conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "astc2bvpyn1c7tr3hy7gg8y72ev3yz",
    "user": "uim2c7d6ergsa7t6a6sd51sds749qg",
    "message": message
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()