# 리스트 내포_Comprehension
import random  # 난수를 만들어 주는 모듈

for i in range(10):
    i


a = []

for i in range(10):
    a.append(i)

print(a)

[i for i in range(10)]  # 리스트
(i for i in range(10))  # 튜플
{i for i in range(10)}  # 셋

print([i for i in range(10)])
print(sum([i for i in range(10)]))

for i in range(5):  # 다섯번 반복
    print(random.randrange(100), end=' ')  # 0~99까지의 난수 발생
print()

for i in range(10):
    print(random.randrange(100), end=' ')
print()

# 문제
# 100보다 작은 난수가 10개 들어있는 리스트 만들기
b = [random.randrange(100) for _ in range(10)]  # _ place holder 라고 부른다 자리만 지킨다.
print(b)

print('-'*50)
# 문제
# 리스트에서 홀수만 뽑아서 별도의 리스트 만들기 (comprehension)

a = []

for i in b:
     if i%2 :
         a.append(i)
         print(i, end=' ')

print()
print(a)
print([i for i in b if i % 2])

print('-'*50)

a1 = [random.randrange(100) for _ in range(10)]
a2 = [random.randrange(100) for _ in range(10)]
a3 = [random.randrange(100) for _ in range(10)]

c = [a1, a2, a3]

print(c)

# 문제
# 2차원 리스트의 전체 합계를 구하세요
s = 0
for i in range(len(c)):
    s += sum(c[i])
print(s)

s = sum(c[0]) + sum(c[1]) + sum(c[2])
print(s)

print(sum([sum(a1), sum(a2), sum(a3)]))

print(sum([sum(i) for i in c]))

print('-' * 50)

# 문제
# 2차원 리스트를 1차원 리스트로 변환하세요
# (반복문으로 먼저 구성한 후에 진행해 봅니다.)

x = []
for i in c:
    for j in i:
        x.append(j)
print(x)

print([j for i in c for j in i])

print('-' * 50)

# 문제 (구글 입사)
# 1 ~ 1000 사이의 정수에 포함된 8의 개수를 구하세요
# 808 -> 2

print(sum([str(i).count('8') for i in range(10000)]))
# for i in range(1000):
#     co = str(i).count('8')
#     print(co)

def count_8(n):
    a1 = n % 10 == 8
    a2 = n // 10 % 10 == 8
    a3 = n // 100 % 10 == 8
    a4 = n // 1000 % 10 == 8

    return a1 + a2 + a3 + a4

print(count_8(808))

print(sum([count_8(i) for i in range(10000)]))

# int, float, str, bool -> basic data type
print(sum([str(i).count('8') for i in range(10000)]))