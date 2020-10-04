# 1. 새파일 생성하기
# f = open('새파일.txt', 'w')
# f.close()

# 2. 파일열기 모드
# w : write  (기존의 것을 덮어쓰기)
# r : read   (읽기)
# a : append (추가쓰기)- 로그

# f = open('test.txt', 'w', encoding='utf-8')
# for i in range(10):       # 0 ~ 9까지
#     data = '%d 째 줄입니다\n' % i
#     f.write(data)
# f.close()

# f = open('test.txt', 'a', encoding='utf-8')
# for i in range(10):       # 0 ~ 9까지
#     data = '%d 째 줄입니다\n' % i
#     f.write(data)
# f.close()

# readlines() 사용해서 읽기
# f = open('test.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#     print(line, end='')
# f.close()

# read() 함수로 읽기
f = open('test.txt', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close()









