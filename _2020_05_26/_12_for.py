# python에는 primitiveType이 없다
# python은 모든 요소가 객체이다
# 그래서 type함수를 사용하면 class로 타입이 나온다
# 변수, 함수, 클래스, 객체 => 객체
# num = 10
# print(num, type(num))

# for문은 list 객체와 많이 쓰인다
# a = ['hong', 'lim', 'jang', 'il']
# for i in a:
#     print(i, end=', ')

# a = [(1, 2), (3, 4), (5, 6)]
# for i in a:
#     print(i)
#
# for (i0, i1) in a:
#     print('%d %d' % (i0, i1))


# 학생 점수가 60점 이상이면 합격, 아니면 불합격
# marks = [90, 25, 67, 48, 80]
# i = 0
# for mark in marks:
#     i = i + 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % i)
#     else:
#         print("%d번 학생은 불합격입니다." % i)


# range()함수와 for문은 함께 많이 사용된다.

# 0~100보다 작을 때까지 반복
# for i in range(0, 100):
#     print(i, end=', ')

# 구구단 출력
# for i in range(2, 10):
#     for j in range(1, 10):
#         print('%dx%d=%d' % (i, j, i*j), end='\t')
#     print()

# for i in range(0, 100, 3):
#     print(i, end=', ')

# for i in range(100, 0, -2):
#     print(i, end=', ')


# 리스트 내포 기능
# result = []
# for i in range(0, 100):
#     result.append(i)
# print(result)

# result = [i for i in range(0, 10)]
# print(result)

# result = [i*3 for i in range(0, 10)]
# print(result)

# result = [i for i in range(0, 10) if i % 2 == 0]
# print(result)

# result = [x*y for x in range(2,10)
#               for y in range(1, 10)]
# print(result)

# 5를 입력하면 아래처럼 출력
# *
# **
# ***
# ****
# *****
while True:
    cnt = int(input("숫자 입력 : "))
    if cnt == -1 : break
    for i in range(1, cnt+1):
        print('*' * i)








