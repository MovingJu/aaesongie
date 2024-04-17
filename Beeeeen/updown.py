import random as rd
import time

def travel(x):
    time.sleep(0.5)
    calcul(x)

def calcul(x):
    choice = int(input(f'\n{lim} 이하의 자연수를 제시해주세요 : '))

    if choice == rdnumber:
        x = x + 1
        print('\n정답!')
        time.sleep(0.5)
        if x == 1:
            print('한번만에 맞추셨어요! 놀라운걸요?\n')
        else:
            print(f'총 {x}번만에 맞추셨어요!\n')
    elif 1 <= choice <= lim:
        if choice < rdnumber:
            x = x + 1
            print('\n업')
            travel(x)
        elif choice > rdnumber:
            x = x + 1
            print('\n다운')
            travel(x)
    else:
        print('\n9999 이하의 자연수만 입력해주세요')
        travel(x)

if __name__ == '__main__':
    print('\n===== 파이썬 업다운 게임 =====')
    lim = int(input("\n최대 숫자를 입력하세요 : "))
    rdnumber = rd.randint(1,lim)
    calcul(0)
