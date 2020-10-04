# a = 10
# b = 20
# a, b = b, a   # (a, b) = (b, a)
# print(a, b)


# 변수의 범위
# ; 전역변수, 지역변수

# a = 1   # 전역변수
#
# def vartest(a):
#     a = a + 1   # 지역변수
#
# vartest(a)
# print(a)


# 함수내에서 전역변수 변경하기
# 1. return값 사용하기      (이것이 더 좋다)
# 2. global 키워드 사용하기 (꼭 필요할 때만 사용)

# a = 1              # 전역변수
# def vartest(a):    # 지역변수
#     a = a + 1
#     return a
#
# a = vartest(a)
# print(a)


a = 1             # 전역변수
def vartest():
    global a      # 전역변수를 함수내에서 사용하겠다
    a = a + 1

vartest()
print(a)







