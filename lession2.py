import random

list = []


def KhoiTao(size: int, seed: int = 10):
    for x in range(size):
         list.append(random.randint(0,seed))


def HienThi(list):
    print('random list: ',end='')
    for x in list:
        print(f'{x} ',end ='')
    print()
def Tong(list):
    sum = 0
    for x in list: sum += x
    return sum
def MaxMin(list):
    max_var = max(list)
    min_var = min(list)

    print(f'max = {max_var}, min = {min_var}')

def TimKiem(x,list):
    # count = 0;
    # for item in list:
    #     if(item ==x): count+=1

    # print(f'so luong {x} : {count}')

    print(f'so luong {x} : {list.count(x)}')


if __name__ == '__main__':
    KhoiTao(10)
    HienThi(list)
    MaxMin(list)
    x = int(input('tim kiem: '))
    TimKiem(x,list)