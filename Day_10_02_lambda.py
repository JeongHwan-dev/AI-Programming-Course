# Day_10_02_lambda.py


def twice(n):
    return n * 2


lamb = lambda n: n * 2      # 한줄짜리 함수, (return) n * 2 리턴 키워드가 생략된 상태


# 문제
# proxy 함수의 코드를 채우세요.
def proxy(f, n):        # callback
    return f(n)


print(twice(3))
print(twice)        # 함수가 할당된 메모리 위치 반환

f = twice       # 변수에 함수를 저장할 수 있다.
print(f)
print(f(3))

print(proxy(twice, 7))
print(proxy(lamb, 7))
print(proxy(lambda n: n*2, 7))  # lambda 의 올바른 사용법

print(lamb(12))
print('-' * 50)

# 문제
# 1.리스트를 오름차순 정렬하세요
# 2.리스트를 내림차순 정렬하세요
a = [5, 9, 1, 3]

# 아래의 두개의 코드는 같은 코드
a.sort()
list.sort(a)

exit(-1)

# a.sort()        # 원본 정렬
# b = sorted(a)   # 복사본 정렬
# print(a)
# print(b)

print(sorted(a))
print(sorted(a)[::-1])
print(sorted(a, reverse=True))


# 문제
# 1. colors 를 오름차순 정렬하세요
# 2. colors 를 내림차순 정렬하세요
def make_lower(s):
    return s.lower()  # lower() : 대문자 -> 소문자로 변환


colors = ['Red', 'green', 'blue', 'YELLOW']
print(sorted(colors))
print(sorted(colors, reverse=True))

print(make_lower('ABC'))
print(make_lower('HeLLo'))

print(sorted(colors, key=make_lower))
print(sorted(colors, key=make_lower, reverse=True))

# 문제
# 람다를 사용해서 코드를 수정하세요.
print(sorted(colors, key=lambda s: s.lower()))
print(sorted(colors, key=lambda s: s.lower(), reverse=True))
print('-' * 50)

# 문제
# colors 를 길이에 따라 정렬하세요 (람다 사용)
# 오름차순과 내림차순 적용하세요. 내림차순은 reverse 옵션을 사용하지 않습니다.
print(sorted(colors, key=lambda s: len(s)))         # 오름차순 정렬
print(sorted(colors, key=len))                      # 오름차순 정렬
print(sorted(colors, key=lambda s: len(s))[::-1])   # 내림차순 정렬
print(sorted(colors, key=lambda s: -len(s)))        # 내림차순 정렬
print('-' * 50)

# 문제
# 튜플로 구성된 리스트를 이름순 정렬, 나이순 정렬하세요.
infos = [('kim', 25), ('han', 71), ('min', 37), ('nam', 13)]

print(sorted((infos)))                     # 이름순 정렬
print(sorted(infos, key=lambda t: t[0]))   # 이름순 정렬
print(sorted(infos, key=lambda t: t[1]))   # 나이순 정렬



