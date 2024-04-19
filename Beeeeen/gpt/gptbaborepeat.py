import random

plin = int(input("몇번 할거임? "))
calcul = []

for _ in range(plin):
    bebe = random.randint(1, 99)
    calcul.append(bebe)

print('결과 :', calcul)

if 7 in calcul:
    print('당첨 ㅊㅊ')
