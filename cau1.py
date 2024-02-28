import math


def isPerfectSquare(x: int) -> bool:
    return (x > 0 and math.sqrt(x) == int(math.sqrt(x))) or x == 0


def generateFibonaci(max: int) -> list:
    f1 = 0
    f2 = 1
    result = []
    while f1 <= max:
        result.append(f1)
        f1, f2 = f2, f1 + f2
    return result



def sumOfNumber(x: int) -> int:
    sum = 0
    while (x > 0):
        sum += int(x % 10)
        x /= 10
    return sum


if __name__ == '__main__':

    # cau a
    n = int(input('n = '))
    squareNumberList = []
    for i in range(0, n):
        if isPerfectSquare(i):
            squareNumberList.append(i)

    # nhanh hon
    # x = 1
    # while x * x <= n:
    #     print(f'{x * x} ' ,end= '')
    #     temp += 1

    print(f'Danh sách các số bao gồm: ', end='')

    if squareNumberList.__len__() == 0:
        print('Không có số nào!')
    else:
        print(squareNumberList)

    # cau b
    fibonacciList = generateFibonaci(n)

    fibonacciAndSquareNumberList = []
    for squareNumber in squareNumberList:
        if fibonacciList.__contains__(squareNumber):
            fibonacciAndSquareNumberList.append(squareNumber)

    fibonacciAndSquareNumberCount = len(fibonacciAndSquareNumberList)
    if fibonacciAndSquareNumberCount > 0:
        print(f'có {fibonacciAndSquareNumberCount} số vừa chính phương, vừa thuộc fibonacci: ',end='')
        print(fibonacciAndSquareNumberList)
    else:
        print('Không có số nào vừa chính phương, vừa thuộc fibonacci',end='')

    print('Danh sách số có giá trị lần lượt là tổng các chữ số của số chính phương có 2 chữ số trở lên: ', end='')

    # cau c
    cList = []
    for squareNumber in squareNumberList:
        if 10 <= squareNumber < 100:
            cList.append(sumOfNumber(squareNumber))

    if (cList.__len__() == 0):
        print('không có số nào!')
    else:
        print(cList)
