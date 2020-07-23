import json
import requests
import re

d1 = {"ip": "8.8.8.8"}
print(d1)
print(type(d1))

d2 = json.dumps(d1)
print(d2)
print(type(d2))

d3 = json.loads(d2)
print(d3)
print(type(d3))
print('-' * 50)

# 문제
# 아래 데이터에서 값에 해당하는 부분문 출력하세요
dt = '{"time": "03:53:25 AM", "milliseconds_since_epoch": 1362196405309, "date": "03-02-2013"}'
dt2 = json.loads(dt)
print(dt2)
print(dt2['time'], dt2['milliseconds_since_epoch'], dt2['date'])

print('-' * 50)

# 기상청 데이터 실습
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
received = requests.get(url)
print(received)
print(received.text)

origin = received.content
print(origin)
print(type(origin))

print()

text = bytes.decode(origin, encoding='utf-8')
print(text)
print('-' * 50)
# 문제
# code와 value에 들어있는 값만 출력하세요
t = json.loads(text)
print(type(t))

for i in range(len(t)):
    print(t[i]['code'], t[i]['value'])

items = json.loads(text)

for item in items:
    print(item['code'], item['value'])

# for i in t[0]:
#     print(i['code'])
# #print(text['code'])
# for text[i] in text:

print([(item['code'], item['value']) for item in items])

# 문제
# 정규표현식을 사용해서 code와 value만 출력하세요
codes = re.findall(r'[0-9]+', text)
values = re.findall(r'[가-힣]+', text)
print(codes)
print(values)

binds = zip(codes, values)
#print(binds)
#print(list(binds))

for c, v in binds:
    print(c, v)
print('-' * 50)

print(re.findall(r'[0-9]+', text))

print(re.findall(r'"code":"[0-9]"', text))
print(re.findall(r'"code":"[0-9]+"', text))

# 문제
# 시도 이름만 출력하세요
print(re.findall(r'"value":"[가-힣]+"', text))
print(re.findall(r'"value":"([가-힣]+)"', text))

# 문제
# code와 value를 한번에 찾으세요
print(re.findall(r'{"code":"([0-9]+)","value":"([가-힣]+)"}', text))