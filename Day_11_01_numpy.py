# Day_11_01_numpy.py
import numpy as np

# 문제
# arange 함수를 사용해서 0 ~ 9까지 10개의 정수를 출력하세요 (3가지)
print(np.arange(0, 10, 1))
print(np.arange(0, 10))
print(np.arange(10))

# ndarray : N-dimensional array
# 배열의 두가지 특징 : 같은 영역, 같은 자료형
print(type(np.arange(10)))

print(np.arange(-5, 5, 1))
print(np.arange(0, 1, 0.2))
print('-' * 30)

a = np.arange(6)
print(a)

# shape : 내부 구조, dtype : 데이터 타입(파이썬 타입 X, 내부 데이터 타입), size : 크기, ndim : 차원
print(a.shape, a.dtype, a.size, a.ndim)     # (6,) int32 6 1
print(np.int32)

# 문제
# 두 가지 방식으로 reshape 을 호출하는 코드를 만드세요.
b = a.reshape(2, 3)
print(b)

b = np.reshape(a, [2, 3])
# b = np.reshape(a, (2, 3))
print(b)

print(b.shape, b.dtype, b.size, b.ndim)     # (2, 3) int32 6 2
print('-' * 50)

# 문제
# 2차원 배열을 1차원으로 변환하세요 (5가지)
print(b.reshape(6))
print(b.reshape(b.size))
print(b.reshape(b.shape[0] * b.shape[1]))   # shape 에 있는 모든 숫자를 곱하면 size 가 된다
print(b.reshape(len(a)))    # len() 함수 사용시 일차원 배열에만 해당
print(b.reshape(-1))

print('-' * 50)

# 문제
# 1차원 배열을 2차원으로 변환하세요 (3가지)
c = b.reshape(-1)

print(c.reshape(3, 2))
print(c.reshape(2, 3))
print(c.reshape(2, -1))
print(c.reshape(-1, 3))
print('-' * 50)

d = list(range(6))          # 리스트
print(d)

d = np.array(range(6))      # 배열
print(d)

print(np.array(range(6)))
print(np.array(range(6), dtype=np.int8))        # 8, 16, 32, 64 비트 (네가지 형태)

print('-' * 50)

g = np.arange(6)

print(g + 1)        # +1을 여섯번 시행했다. +1을 배열 전체에 전파 -> broadcast (방송 송출 개념 생각)
print(g ** 2)
print(g > 2)
print(type(g > 2))
print((g > 2).dtype)
print()

h = g.reshape((2, 3))       # broadcast 연산은 차원을 가리지 않는다. 모든 차원에서 사용가능하다.
print(h)
print(h + 1)
print(h ** 2)
print(h > 2)

print('-' * 50)

# 배열 연산
# 배열 연산을 할 때에는 size 가 같아야 한다.
print(g + g)        # vector
print(h + h)

print(np.sin(g))        # universal function
print(np.sin(h))

print('-' * 50)

a1 = np.arange(3)
a2 = np.arange(6)
a3 = np.arange(3).reshape(1, 3)
a4 = np.arange(3).reshape(3, 1)
a5 = np.arange(6).reshape(2, 3)

# print(a1 + a2)        # error
print(a1 + a3)          # (3,) => (1, 3)
print(a1 + a4)          # (1, 3) + (3, 1) : broadcast + broadcast
print(a1 + a5)          # (1, 3) + (2, 3) : broadcast + vector
print()

# 문제
# 아래 결과를 에러 나는지 예측한 이후에 실제 결과와 비교하세요.
# 두 개 중에 하나가 1이 있거나, 두 개가 같거나 하면 연산 가능
# print(a2 + a3)        # (1, 6) + (1, 3) : error
print(a2 + a4)          # (1, 6) + (3, 1) -> (3, 6) : broadcast + broadcast
# print(a2 + a5)        # (1, 6) + (2, 1) : error

print(a3 + a4)          # (1, 3) + (3, 1) -> (3, 3) : broadcast + broadcast
print(a3 + a5)          # (1, 3) + (2, 3) -> (2, 3 : broadcast + vector

# print(a4 + a5)        # (3, 1) + (2, 3) : error

