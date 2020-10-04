
# 회수 입력받고 회수만큼 반복문 처리
# treeHit = 0
# strCnt = input('나무를 찍을 회수 입력 : ')
# cnt = int(strCnt)
# while treeHit < cnt:
#     treeHit = treeHit + 1
#     print('나무를 %d번 찍었습니다.' % treeHit)
#     if treeHit == cnt:
#         print('나무 넘어갑니다')


# 사칙 연산
# print('*'*10 + '사칙연산을 실행합니다' + '*'*10)
# menu = """
# [메뉴를 선택하세요]
# 1. Add
# 2. Sub
# 3. Mul
# 4. Div
#
# 5. exit
# """
# while True:
#     print(menu)
#     op = int(input('연산 선택 : '))
#     num0 = int(input('첫 번째 숫자 입력 : '))
#     num1 = int(input('두 번째 숫자 입력 : '))
#
#     result = 0
#     if op==1:
#         result = num0 + num1
#     elif op==2:
#         result = num0 - num1
#     elif op==3:
#         result = num0 * num1
#     elif op==4:
#         result = num0 / num1
#     elif op==5:
#         print('연산을 종료합니다')
#         break
#     else:
#         print('잘 못 선택했습니다')
#
#     print('결과는 ' + str(result) + '입니다')
#     print('결과는 %d입니다' % result)


# continue문
num = 0
while num < 10:
    num = num + 1
    if num%2==0:
        continue
    print(num, end=', ')








