import random as rd
import sys

girlitems = {
    '여자' : 1,
    '김지우' : 999
}

def gotcha(items):
    randnum = rd.randint(1, 1000)
    tempnum = 0
    for i, j in items.items():
        tempnum += j
        if randnum <= tempnum:
            return i

def main(items):
    print('\n수많은 김지우 중 여자를 뽑아라! (0.1%)')
    wide = int(input('\n몇 번 뽑을 거에요? : '))
    count = 0
    for i in range(wide):
        count += 1
        tempfun = gotcha(items)
        if tempfun == '여자':
            print(f'{count}회 째, {tempfun}')
            print('당첨!')
            sys.exit()
        else:
            print(f'{count}회 째, {tempfun}')
    sys.exit()

main(girlitems)