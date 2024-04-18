import random as rd
import sys
import time

def main():
    print('\n===== 파이썬 러시안 룰렛 =====')
    print('\n1. 1 vs 1')
    print('2. AI전')

    select = input('\n플레이 방식을 선택하세요 (번호) : ')

    if select == '1':
        onevsone()
    elif select == '2':
        aivsone()
    else:
        print('\n나열된 방식 중 선택하세요')
        time.sleep(1)
        main()

def onevsone():
    bull = []
    nobu = 0
    realbul = rd.randint(0,5)
    
    for i in range(0,6):
        if i == realbul:
            bull.append('1')
        else:
            bull.append('0')

    print('\n\n===== 러시안 룰렛 [1vs1전] =====')
    time.sleep(1)
    print('\n선을 정합니다...')
    time.sleep(2)
    takeposi = rd.randint(1,2)
    if takeposi == 1:
        print(f'\n{takeposi}p의 선!')
        time.sleep(1)
        firplay(bull,nobu)
    else:
        print(f'\n{takeposi}p의 선!')
        time.sleep(1)
        secplay(bull,nobu)

def firplay(bull,nobu):
    time.sleep(1)
    print(f'\n== 1p의 차례! ==      남은 탄환 : {6 - nobu}/6')
    print('\n1. 1p (자신)')
    print('2. 2p')
    print('\n3. 메뉴로 나가기')
    choice = input('\n겨냥할 사람을 선택하세요 (번호) : ')
    if choice == '1':
        ftfplay(bull,nobu)
    elif choice == '2':
        ftsplay(bull,nobu)
    elif choice == '3':
        main()
    else:
        print('\n나열된 인원 중 선택하세요')
        time.sleep(1)
        firplay(bull,nobu)

def secplay(bull,nobu):
    time.sleep(1)
    print(f'\n== 2p의 차례! ==       남은 탄환 : {6 - nobu}/6')
    print('\n1. 1p')
    print('2. 2p (자신)')
    print('\n3. 메뉴로 나가기')
    choice = input('\n겨냥할 사람을 선택하세요 (번호) : ')
    if choice == '1':
        stfplay(bull,nobu)
    elif choice == '2':
        stsplay(bull,nobu)
    elif choice == '3':
        main()
    else:
        print('\n나열된 인원 중 선택하세요')
        time.sleep(1)
        secplay(bull,nobu)

def ftsplay(bull,nobu):
    if bull[nobu] == '1':
        print('\n탕')
        time.sleep(2)
        print('\n2p가 죽었습니다. 1p의 승리입니다')
        reonevsone(nobu)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n2p가 죽지 않았습니다. 턴이 넘어갑니다')
        secplay(bull,nobu)

def ftfplay(bull,nobu):
    if bull[nobu] == '1':
        print('\n탕')
        time.sleep(2)
        print('\n1p가 죽었습니다. 2p의 승리입니다')
        reonevsone(nobu)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n1p가 죽지 않았습니다. 턴이 유지됩니다')
        firplay(bull,nobu)

def stfplay(bull,nobu):
    if bull[nobu] == '1':
        print('\n탕')
        time.sleep(2)
        print('\n1p가 죽었습니다. 2p의 승리입니다')
        reonevsone(nobu)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n1p가 죽지 않았습니다. 턴이 넘어갑니다')
        firplay(bull,nobu)

def stsplay(bull,nobu):
    if bull[nobu] == '1':
        print('\n탕')
        time.sleep(2)
        print('\n2p가 죽었습니다. 1p의 승리입니다')
        reonevsone(nobu)
    else:
        nobu = nobu + 1
        print('\n탕')
        time.sleep(2)
        print('\n2p가 죽지 않았습니다. 턴이 유지됩니다')
        secplay(bull,nobu)

def aivsone():
    bull = []
    nobu = 0
    realbul = rd.randint(0,5)
    
    for i in range(0,6):
        if i == realbul:
            bull.append('1')
        else:
            bull.append('0')

    print('\n\n===== 러시안 룰렛 [AI전] =====')
    user(bull,nobu)

def user(bull,nobu):
    time.sleep(1)
    print(f'\n== 당신의 차례! ==     {6 - nobu}/6')
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
    if bull[nobu] == '1':
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
    if bull[nobu] == '1':
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
    if bull[nobu] == '1':
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
    if bull[nobu] == '1':
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

def reonevsone(nobu):
    time.sleep(1)
    print(f'실탄은 {nobu + 1}번째에 있었습니다')
    time.sleep(2)
    print('\n1. 다시하기')
    print('2. 메뉴로 나가기')
    select1 = input('\n다시하시겠어요? (번호) : ')
    if select1 == '1':
        onevsone()
    elif select1 == '2':
        main()

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

if __name__ == "__main__":
    main()
