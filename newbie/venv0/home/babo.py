import random

player_input = input("할거임? (y or n)")
def randnum():
    if player_input == y:
        bebe = random.randint(0,98)
        return bebe
    elif player_input == n:
        bebe = "잘가요"
        return bebe
    else:
        bebe = "넌 뭐야"
        return bebe
result = player_input()
print('결과 : ', result)

if result == 7:
    print('오 님 좀 쩌는 듯?')
else: print('허접이시네요')
