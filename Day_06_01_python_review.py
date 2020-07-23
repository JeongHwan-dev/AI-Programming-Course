a = list(range(10))
print(a)

# 첫번째 방법
a.reverse()
print(a)

a.sort()
print(a)

print(a[::-1])

a.sort()
print(a)

for i in range(len(a)):
    print(a[len(a) - 1 - i], end=' ')
print()

for i in range(len(a)):
    print(a[-i -1], end=' ')
print()

for i in reversed(range(len(a))):
    print(a[i], end=' ')
print()

for i in reversed(a):
    print(i, end=' ')
print()
print('-' * 50)

b = a # 얕은 복사(shallow copy)
c = a[:] # 깊은 복사 (deep copy)
d = a.copy()

e = []

for i in a:
    e.append(i)

a[0] = 99

print(a)
print(b)
print(c)
print(d)
print(e)
print('-' * 50)

def max2(a, b):
   if a > b:
       b = a
   return b

max = max2(2, 1)
print(max)

print('-' * 50)

def max4(a, b, c, d):
    # if a < b :
    #     a = b
    # if a < c:
    #     a = c
    # if a < d :
    #     a = d
    # return a

    # 복면가왕
    # return max2(max2(a, b), max2(c, d))

    # 한국시리즈
    return max2(max2(max2(a, b), c), d)

print(max4(1, 3, 5, 7))
print(max4(3, 5, 7, 1))
print(max4(5, 7, 1, 3))
print(max4(7, 1, 3, 5))


