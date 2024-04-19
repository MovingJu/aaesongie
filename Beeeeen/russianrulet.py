import random as rd
import sys
import time

def main():
    print('\n===== 파이썬 러시안 룰렛 =====')
    print('\n1. 1vs1')
    print('2. 1vs1 확장판')
    print('3. AI전')
    print('4. 종료')

    select = input('\n플레이 방식을 선택하세요 (번호) : ')

    if select == '1':
        onevsone()
    elif select == '2':
        dlcver()
    elif select == '3':
        aivsone()
    elif select == '4':
        sys.exit()
    else:
        print('\n나열된 방식 중 선택하세요')
        time.sleep(1)
        main()

def onevsone():
    dlc = 0
    bull = []
    nobu = 0
    realbul = rd.randint(0,5)
    
    for i in range(0,6):
        if i == realbul:
            bull.append(1)
        else:
            bull.append(0)

    print('\n\n===== 러시안 룰렛 [1vs1전] =====')
    time.sleep(1)
    print('\n선을 정합니다...')
    time.sleep(2)
    takeposi = rd.randint(1,2)
    if takeposi == 1:
        print(f'\n{takeposi}p의 선!')
        time.sleep(1)
        firplay(bull,nobu,dlc)
    else:
        print(f'\n{takeposi}p의 선!')
        time.sleep(1)
        secplay(bull,nobu,dlc)

def dlcver():                       # 이거 구상한다고 1교시 다 씀
    dlc = 1
    bull = []
    realbul = []
    nobu = 0
    print('\n\n===== 러시안 룰렛 [1vs1 확장판] =====')
    time.sleep(1)
    maxbul = int(input('\n최대 탄환 수를 설정하세요 : '))
    selbul = int(input('실탄 개수를 설정하세요 : '))
    if maxbul >= selbul:
        for i in range(0,maxbul):
            bull.append(0)
    else:
        print('\n실탄 개수는 최대 탄환 수보다 작아야 합니다')
        time.sleep(1)
        dlcver()
    for m in range(0,selbul):
        realbul.append(rd.randint(0,maxbul-1))
    while len(set(realbul)) < selbul:
        realbul = list(set(realbul))
        realbul.append(rd.randint(0,maxbul-1))
    for j in range(0,selbul):
        bull[realbul[j]] = 1
    time.sleep(1)
    print('\n선을 정합니다...')
    time.sleep(2)
    takeposi = rd.randint(1,2)
    if takeposi == 1:
        print(f'\n{takeposi}p의 선!')
        time.sleep(1)
        firplay(bull,nobu,dlc)
    else:
        print(f'\n{takeposi}p의 선!')
        time.sleep(1)
        secplay(bull,nobu,dlc)

def firplay(bull,nobu,dlc):
    time.sleep(1)
    print(f'\n== 1p의 차례! ==      남은 탄환 : {len(bull) - nobu}/{len(bull)}')
    print('\n1. 1p (자신)')
    print('2. 2p')
    print('\n3. 메뉴로 나가기')
    choice = input('\n겨냥할 사람을 선택하세요 (번호) : ')
    if choice == '1':
        ftfplay(bull,nobu,dlc)
    elif choice == '2':
        ftsplay(bull,nobu,dlc)
    elif choice == '3':
        main()
    else:
        print('\n나열된 인원 중 선택하세요')
        time.sleep(1)
        firplay(bull,nobu,dlc)

def secplay(bull,nobu,dlc):
    time.sleep(1)
    print(f'\n== 2p의 차례! ==       남은 탄환 : {len(bull) - nobu}/{len(bull)}')
    print('\n1. 1p')
    print('2. 2p (자신)')
    print('\n3. 메뉴로 나가기')
    choice = input('\n겨냥할 사람을 선택하세요 (번호) : ')
    if choice == '1':
        stfplay(bull,nobu,dlc)
    elif choice == '2':
        stsplay(bull,nobu,dlc)
    elif choice == '3':
        main()
    else:
        print('\n나열된 인원 중 선택하세요')
        time.sleep(1)
        secplay(bull,nobu,dlc)

def ftsplay(bull,nobu,dlc):
    if bull[nobu] == 1:
        print('\n탕')
        time.sleep(2)
        print('\n2p가 죽었습니다. 1p의 승리입니다')
        reonevsone(nobu,dlc)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n2p가 죽지 않았습니다. 턴이 넘어갑니다')
        secplay(bull,nobu,dlc)

def ftfplay(bull,nobu,dlc):
    if bull[nobu] == 1:
        print('\n탕')
        time.sleep(2)
        print('\n1p가 죽었습니다. 2p의 승리입니다')
        reonevsone(nobu,dlc)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n1p가 죽지 않았습니다. 턴이 유지됩니다')
        firplay(bull,nobu,dlc)

def stfplay(bull,nobu,dlc):
    if bull[nobu] == 1:
        print('\n탕')
        time.sleep(2)
        print('\n1p가 죽었습니다. 2p의 승리입니다')
        reonevsone(nobu,dlc)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n1p가 죽지 않았습니다. 턴이 넘어갑니다')
        firplay(bull,nobu,dlc)

def stsplay(bull,nobu,dlc):
    if bull[nobu] == 1:
        print('\n탕')
        time.sleep(2)
        print('\n2p가 죽었습니다. 1p의 승리입니다')
        reonevsone(nobu,dlc)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n2p가 죽지 않았습니다. 턴이 유지됩니다')
        secplay(bull,nobu,dlc)

def aivsone():
    bull = []
    nobu = 0
    realbul = rd.randint(0,5)
    
    for i in range(0,6):
        if i == realbul:
            bull.append(1)
        else:
            bull.append(0)

    print('\n\n===== 러시안 룰렛 [AI전] =====')
    user(bull,nobu)

def user(bull,nobu):
    time.sleep(1)
    print(f'\n== 당신의 차례! ==     {len(bull) - nobu}/{len(bull)}')
    print('\n1. 상대')
    print('2. 자신')
    print('\n3. 메뉴로 나가기')
    choice = input('\n겨냥할 사람을 선택하세요 (번호) : ')
    if choice == '1':
        shother(bull,nobu)
    elif choice == '2':
        shmyself(bull,nobu)
    elif choice == '3':
        main()
    else:
        print('\n나열된 인원 중 선택하세요')
        time.sleep(1)
        user(bull,nobu)
    
def shother(bull,nobu):
    if bull[nobu] == 1:
        print('\n탕')
        time.sleep(2)
        print('\n상대방이 죽었습니다. 당신의 승리입니다')
        reaivsone(nobu)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n상대방이 죽지 않았습니다. 턴이 넘어갑니다')
        time.sleep(2)
        computer(bull,nobu)

def shmyself(bull,nobu):
    if bull[nobu] == 1:
        print('\n탕')
        time.sleep(2)
        print('\n당신이 죽었습니다. 당신의 패배입니다')
        reaivsone(nobu)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n당신은 죽지 않았습니다. 턴이 돌아옵니다')
        time.sleep(2)
        user(bull,nobu)

def computer(bull,nobu):
    print('\n== 컴퓨터의 차례 ==')
    time.sleep(1)
    compshot = rd.randint(0,1)
    if compshot == 0:
        shmine(bull,nobu)
    elif nobu == 5:
        shmine(bull,nobu)
    else:
        shyours(bull,nobu)

def shmine(bull,nobu):
    if bull[nobu] == 1:
        print('\n컴퓨터는 당신을 향해 쐈습니다')
        time.sleep(1)
        print('\n탕')
        time.sleep(2)
        print('\n당신이 죽었습니다. 당신의 패배입니다')
        reaivsone(nobu)
    else:
        nobu = nobu + 1
        print('\n컴퓨터는 당신을 향해 쐈습니다')
        time.sleep(1)
        print('\n탕')
        time.sleep(2)
        print('\n당신은 죽지 않았습니다. 당신의 턴입니다')
        time.sleep(2)
        user(bull,nobu)

def shyours(bull,nobu):
    if bull[nobu] == 1:
        print('\n상대는 자신을 향해 쐈습니다')
        time.sleep(1)
        print('\n탕')
        time.sleep(2)
        print('\n상대가 죽었습니다. 당신의 승리입니다')
        reaivsone(nobu)
    else:
        nobu = nobu + 1
        print('\n상대는 자신을 향해 쐈습니다')
        time.sleep(1)
        print('\n탕')
        time.sleep(2)
        print('\n상대는 죽지 않았습니다. 상대방의 턴입니다')
        time.sleep(2)
        computer(bull,nobu)

def reonevsone(nobu,dlc):
    time.sleep(1)
    print(f'실탄은 {nobu + 1}번째에 있었습니다')
    time.sleep(2)
    print('\n1. 다시하기')
    print('2. 메뉴로 나가기')
    select1 = input('\n다시하시겠어요? (번호) : ')
    if select1 == '1':
        if dlc == 0:
            onevsone()
        else:
            dlcver()
    elif select1 == '2':
        main()
    else:
        print('\n나열된 방식 중 선택하세요')
        time.sleep(1)
        reonevsone(nobu,dlc)

def reaivsone(nobu):
    time.sleep(1)
    print(f'실탄은 {nobu + 1}번째에 있었습니다')
    time.sleep(2)
    print('\n1. 다시하기')
    print('2. 메뉴로 나가기')
    select1 = input('\n다시하시겠어요? (번호) : ')
    if select1 == '1':
        aivsone()
    elif select1 == '2':
        main()
    else:
        print('\n나열된 방식 중 선택하세요')
        time.sleep(1)
        reaivsone(nobu)

if __name__ == "__main__":
    main()
