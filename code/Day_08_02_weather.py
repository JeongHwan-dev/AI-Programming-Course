import requests
import re

f = open('data/weather.csv', 'w', encoding='utf-8')
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=131'
received = requests.get(url)
# print(received)
# print(received.text)

# 문제
# city만 찾아보세요
# city = re.findall(r'<city>([가-힣]+)</city>', received.text)
# print(city)

# 문제
# location을 찾아보세요
# re.DOTALL : 개행문자 무시.
# .+ : 탐용적 (greedy)
# .+? : 비탐욕적(non-greedy)
# re.DOTALL 내가 찾는것이 여러줄에 걸쳐 있을 때
locations = re.findall(r'<location wl_ver="3">.+?</location>', received.text, re.DOTALL)
print(len(locations))
# print(locations)
# for loc in locations:
    # print(loc)

# print('='*50)

# 문제
# province와 city를 찾아보세요
for loc in locations:
    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    # print(prov[0], city[0])

    # 문제
    # province와 city를 한번에 찾아보세요 (깔끔하게 출력 포함)
    prov_city = re.findall(r'<province>(.+)</province>.+<city>(.+)</city>', loc, re.DOTALL)
    prov, city = prov_city[0]
    # print(prov_city[0])
    #print(prov, city)


    # 문제
    # data를 찾아보세요
    data = re.findall(r'<data>.+?</data>', loc, re.DOTALL)
    # print(len(data))

    for datum in data:
        # mode = re.findall(r'<mode>(.+)</mode>', datum)
        # tmEF = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        # wf = re.findall(r'<wf>(.+)</wf>', datum)
        # tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
        # tmax = re.findall(r'<tmx>(.+)</tmx>', datum)
        # rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)
        # print(prov[0], city[0], mode[0], tmEF[0], wf[0], tmn[0], tmax[0], rnSt[0])
        pattern = r'<.+>(.+)</.+>'

        all_info = re.findall(pattern, datum)
        mode, tmEF, wf, tmn, tmax, rnSt = all_info  # unpacking
        # print(prov, city, mode, tmEF, wf, tmn, tmax, rnSt, file=f, sep=',')
        # print(prov, city, all_info)
        # print(prov, city, all_info)
        print(prov, city, *all_info)

        # row = '{},{},{},{},{},{},{},{}\n'.format(prov, city, mode, tmEF, wf, tmn, tmax, rnSt)
        # f.write(row)

        f.write(prov + ',')
        f.write(city + ',')
        f.write(mode + ',')
        f.write(tmEF + ',')
        f.write(wf + ',')
        f.write(tmn + ',')
        f.write(tmax + ',')
        f.write(rnSt + '\n')


# 문제
# 기상청 데이터 파일을 저장하세요 (원본대로 읽을 수 있는 형태로 저장)
# weather.csv

f.close()


