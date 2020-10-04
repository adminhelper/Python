# python의 함수는 여러 개의 값을 반환할 수 있다.
# 그러나 사실은 1개의 객체만 리턴되는 것이다
# 여러 개의 값이 tuple객체로 묶여져서 사실은 1개의 tuple객체가
# 리턴되는 것이다

def viewMenu():
    menu = """
    1. Add
    2. Sub
    3. Mul
    4. Div
    
    5. exit
    """
    print(menu)


def getNumber(strView):
    return int(input(strView))


def calcArith(num0, num1):
    return (num0+num1, num0-num1, num0*num1, num0/num1)


def inputValue():
    num0 = getNumber('첫 번째 숫자 입력 : ')
    num1 = getNumber('두 번째 숫자 입력 : ')
    return (num0, num1)


(num0, num1) = inputValue()
(radd, rsub, rmul, rdiv) = calcArith(num0, num1)
print('Add 결과는 ' + str(radd) + '입니다')
print('Sub 결과는 ' + str(rsub) + '입니다')
print('Mul 결과는 ' + str(rmul) + '입니다')
print('Div 결과는 ' + str(rdiv) + '입니다')
