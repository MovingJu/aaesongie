import random as rd
import time
import sys

gotchaitems = {
    '☆' : 65,
    '☆☆' : 25,
    '☆☆☆' : 8,
    '★★★' : 2,
}

def main():
    print('\n===== 가챠 똥망겜에 오신 걸 환영합니다! =====\n')
    for i,j in gotchaitems.items():
        print(f'{i} : {j}%')
    count = 0
    yesorno(count)

def yesorno(count):
    selectdict = {
        '1' : gotcha,
        '2' : outgame
    }
    # print('\n1 : yes\n2 : no')
    playeryesorno = input(f'\n{count}회쨰, 하시겠어요? :')
    selected = selectdict.get(playeryesorno)
    if selected:
        selected(count)
    else:
        print('올바른 번호를 입력하세요')
        time.sleep(1)
        yesorno(count)

def outgame():
    print('\n게임을 종료합니다...')
    time.sleep(1)
    sys.exit()

def gotcha(count):
    count = count + 1
    randomnum = rd.randint(1,100)
    sumper = 0
    for i, j in gotchaitems.items():
        sumper += j
        if randomnum <= sumper:
            print(i)
            break
    yesorno(count)

if __name__ == '__main__':
    main()
