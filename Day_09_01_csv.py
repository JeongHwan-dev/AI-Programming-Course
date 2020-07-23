# Day_09_01_csv.py
import csv


# 문제
# weather.csv 파일을 읽어서 결과를 반환하세요
def read_csv_1():
    f = open('data/weather.csv', 'r', encoding='utf-8')

    # rows = []
    # for line in f:
    #     # print(line.strip().split(','))
    #     rows.append(line.strip().split(','))
    rows = [line.strip().split(', ') for line in f]

    f.close()
    return rows


rows = read_csv_1()

# 문제
# rows를 이전에 출력했던 형태로 출력하시오.
# for row in rows:
#     for col in row:
#         print(col, end='')
#
#     print()

def read_csv_2():
    f = open('data/weather.csv', 'r', encoding='utf-8')

    rows = []
    for line in csv.reader(f):
        rows.append(line)

    f.close()
    return rows

rows = read_csv_1()
rows = read_csv_2()

