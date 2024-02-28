import random

def KhoiTao(seed = 10):
    global a, b, c
    a = random.randint(0, seed)
    b = random.randint(0, seed)
    c = random.randint(0, seed)
    
def HienThi():
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

def Tong(): return a + b + c


def MaxMin():
    min_var = min(a, b, c)
    max_var = max(a, b, c)

    print('max = ', max_var)
    print('min = ', min_var)


def TimKiem(x:int):
    exist = x == a or x == b or x == c
    if exist:
        print(f'co ton tai {x}')
    else:
        print(f'khong ton tai {x}')


if __name__ == '__main__':
    KhoiTao()
    HienThi()
    MaxMin()
    print(f'tong = {Tong()}')
    x = int(input('gia tri can tim: x = '))
    TimKiem(x)
