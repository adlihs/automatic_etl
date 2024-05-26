import os
import http.client, urllib
# Access variables
pushover_key = 'ucz4hngocjn2zub71upf89ir3ho7z8' #os.getenv('pushover_userkey')
pushover_token = 'a6avhx9pay8qa8fg3yeoxek225ci7h' #os.getenv('pushover_token')
print(pushover_key)

conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
             urllib.parse.urlencode({
                 "token": pushover_token,
                 "user": pushover_key,
                 "message": "Github actions...!",
             }), {"Content-type": "application/x-www-form-urlencoded"})
conn.getresponse()