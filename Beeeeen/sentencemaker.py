import random as rd
'''
subj = ['나는', '내가', '이 몸은', '짐은', '제가', '저는']
comp = ['사람', '천재', '바보', '강아지', '고양이', '신']
verb = ['입니다', '이니라', '랄까?', '인데요', '아닙니다', '좋아합니다']
'''
elem = [['나는', '내가', '이 몸은', '짐은', '제가', '저는'],
        ['사람', '천재', '바보', '강아지', '고양이', '신'],
        ['입니다', '이니라', '랄까?', '인데요', '아닙니다', '좋아합니다']]

player_input = int(input('몇번 돌릴 거에요? : '))

def dice():
    rsubj = elem[0][rd.randint(0,5)]
    rcomp = elem[1][rd.randint(0,5)]
    rverb = elem[2][rd.randint(0,5)]
    return f'{rsubj} {rcomp} {rverb}.'

for i in range(0,player_input):
    print(dice())
