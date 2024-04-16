import random
import sys

def randnum():
    player_input = input("할거임? (y or n)")
    if player_input == 'y':
        bebe = random.randint(1,99)
        return bebe
    elif player_input == 'n':
        print('잘가요')
        sys.exit()
    else:
        print("넌 뭐야")
        sys.exit()

result = randnum()
print('결과 : ', result)

if result == 7:
    print('오')
else: print('허접')