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


def calcArith(sel, num0, num1):
    result = 0
    if sel == 1:
        result = num0 + num1
    elif sel == 2:
        result = num0 - num1
    elif sel == 3:
        result = num0 * num1
    elif sel == 4:
        result = num0 / num1

    return result


viewMenu()
sel = getNumber('번호를 선택 : ')
num0 = getNumber('첫 번째 숫자 입력 : ')
num1 = getNumber('두 번째 숫자 입력 : ')
result = calcArith(sel, num0, num1)
print('결과는 ' + str(result) + '입니다')

