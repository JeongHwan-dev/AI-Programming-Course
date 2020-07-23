# Day_12_01_numpy.py
import numpy as np

print(np.zeros(3))
print(np.ones(3))
print(np.full(3, fill_value=-1))

print(np.zeros(6).reshape(2, 3))
print(np.zeros([2, 3]))
print(np.zeros([2, 3]).dtype)
print(np.zeros([2, 3], dtype=np.int32))
print('-' * 50)

print(np.random.random(5))
print(np.random.random([5, 5]))     # 0 ~ 1
print(np.random.randn(5))
print(np.random.randn(5, 5))       # n : Normal Distribution
print(np.random.randn(5 * 5).reshape(5, 5))
print(np.random.uniform(0, 10, 5))      # 0에서 부터 10보다 작은 범위에서 5개 만들기
print(np.random.choice(range(10), 15))  # 0 ~ 9, 15개 뽑아내기
print(np.random.randint(0, 10, 5))      # 정수 뽑아내기
print('-' * 50)

np.random.seed(41)
a = np.random.choice(range(10), 15).reshape(3, 5)
print(a)

print(np.sum(a))        # 전체 합계
print(a.sum())

print(np.sum(a))
# axis : 축
print(np.sum(a, axis=0))        # 열(수직)
print(np.sum(a, axis=1))        # 행(수평)

# 문제
# 2차원 배열에서 가장 큰 값과 가장 작은 값을 구하세요
print(np.min(a, axis=0))
print(np.min(a, axis=1))

print(np.mean(a))

# np.argmax : 가장 큰 수의 출력
print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))
print('-' * 50)

print(a)
print(a[0], a[-1])

# a[0] = -1
# print(a)

# 문제
# 2차원 배열을 거꾸로 출력하세요.
print(a[::-1])          # 행으로 뒤집기
print(a[::-1][::-1])    # 다시 처음 상태로

b = a[::-1]
c = b[::-1]
print(c)

print(a[::-1, ::-1])        # fancy indexing

# 문제
# 2차원 배열의 처음과 마지막 번째의 값을 -1로 바꾸세요.
# a[0][0] = -1
# a[-1][-1] = -1

a[0, 0] = -1
a[-1, -1] = -1

a[0, 1] = -2
a[-1, -2] = -2
print(a)
print('-' * 50)

# 문제
# 속은 0이고 테두리가 1로 채워진 5행 5열 배열을 만드세요
# 첫번째 방법
a = np.full(25, fill_value=1).reshape(5, 5)

for i in range(3):
    for j in range(3):
        a[i+1, j+1] = 0

print(a)

# 두번째 방법
b = np.zeros([5, 5], dtype=np.int32)
b[0, :] = 1     # = b[0]
b[-1, :] = 1    # = b[-1]
b[:, 0] = 1
b[:, -1] = 1

print(b)

# 문제
# 아래 코드에 펜시 인덱싱을 적용해서 속만 0으로 채우세요.
c = np.ones([5, 5], dtype=np.int32)

c[1:-1, 1:-1] = 0
print(c)
print('-' * 50)

# 문제
# 아래처럼 출력하세요. (transpose, 열 우선)
d = np.arange(20).reshape(4, 5)

for i in range(4):          # 4행
    for j in range(5):      # 5열
        print('({}, {}) {}'.format(i, j, d[i, j]), end=' ')
    print()

for i in range(d.shape[0]):          # 4행
    for j in range(d.shape[1]):      # 5열
        print('{:2}'.format(d[i, j]), end=' ')
    print()

for i in range(d.shape[1]):          # 5행
    for j in range(d.shape[0]):      # 4열
        print('{:2}'.format(d[j, i]), end=' ')
    print()

for i in range(d.shape[1]):
    print(d[:, i])

print(d.transpose())

print('-' * 50)

e = np.arange(12)
print(e)

print(e[0], e[3])
print(e[[0, 3]])

i = [0, 3, 5, 3]
print(e[i])

f = e.reshape(3, 4)
print(f)

# 문제
# 2차원 배열에 대해 인덱스 배열을 적용해 보세요
print(f[[0, -1]])

# 문제
# 5행 5열 크기의 단위 행렬을 만드세요.
# 단위 행렬 : 전체가 0인데, 대각선에만 1이 들어간 행렬
x = np.zeros([5, 5], dtype=np.int32)

for i in range(5):
    for j in range(5):
        if i == j:
            x[i][j] = 1

print(x)

x = np.zeros((5, 5), dtype=np.int32)

for i in range(x.shape[0]):
    x[i, i] = 1

print(x)

g = np.zeros([5, 5], dtype=np.int32)
#
# for i in range(5):
#     g[i, i] = 1

# g[[0, 1, 2], [0, 1, 2]] = 1
g[range(5), range(5)] = 1
print(g)
print('-' * 30)

t = np.int32([1, 5, 2, 7, 4])
bools = [True, False, False, True, False]

print(t[bools])

for i in range(len(t)):
    if bools[i]:
        print(t[i])


