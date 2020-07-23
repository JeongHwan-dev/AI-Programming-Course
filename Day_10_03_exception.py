# Day_10_03_exception.py

try:                    # Exception 을 처리하기 위한 범위
    a = [1, 3, 5]
    print(a[0])
    print(a[len(a)])
except IndexError as e:
    print('IndexError')
    print(e)

# 문제
# 아래 코드에서 발생하는 예외를 처리하세요
try:
    b = '3.14'
    print('b : ', int(b))
except ValueError as e:
    print('ValueError')
    print(e)
# except:
#     print('unknown')


while True:
    try:
        number = input('input integer : ')
        number = int(number)
        break
    except ValueError:
        print('정수를 입력하세요')


print(int(number) * 7 % 10)

