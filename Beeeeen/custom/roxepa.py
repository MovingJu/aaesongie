import random as rd
import time

roxepa_list = ['가위', '바위', '보']
battle_dict = {'가위' : {'바위' : '패배!',
                         '보' : '승리!'},
               '바위' : {'가위' : '승리!',
                         '보' : '패배!'},
               '보' : {'가위' : '패배!',
                       '바위' : '승리!'}}

def computer_input():
    c_input = rd.randint(0,2)
    return roxepa_list[c_input]

def player_input():
    p_input = input('무엇을 낼 건가요? : ')
    if p_input in roxepa_list:
        return p_input
    else:
        print('올바르지 않습니다')
        time.sleep(1)
        return player_input()

def main():
    while True:
        print('\n===== 가위바위보 게임 =====')
        p_collect = player_input()
        c_collect = computer_input()
        print('컴퓨터 :', c_collect)
        if p_collect == c_collect:
            print('무승부!')
        else:
            print(battle_dict[p_collect][c_collect])
        time.sleep(2) 

main()