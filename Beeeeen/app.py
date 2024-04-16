'''
print('이동주'[2:3])

중고차 = ['ㄱㄱ', 'ㄴㄴ', [1234,2345]]
중고차[2][0] = 10000
print(중고차[2][0])

중고차2 = { '강상원' : '100' , '남지훈' : '101' }
print(중고차2['남지훈'])

재고 = ['K5', 'BMW', 'Tico']
if 'K5' in 재고 :
    print('주문가능')

for i in range(1,3):
    print('조성민멍청이')

for i in 재고:
    print(i)

재고 = [10,20,30]
for i in 재고:
    print(i+1)

for i in range(1,101):
    for j in range(1,101):
        m = i*j
        print(f'print({i}*{j})={m}')

def dlehdwn():
    print('안녕하세요 중고차신뢰딜러 차은우입니다')
    print('현재 딜러할인 최대 적용중이라 쪽지로 문의주십쇼')

dlehdwn()
'''
def math(x,y):
    result = x**2+2*x+1 + y
    # result = int(result)
    print(result)

def math2(x,y):
    return x**2+2*x+1 + y           # 이거 개사기

key = [1, 2]
key[0] = input('x값 입력해 ')
key[1] = input('y값 입력해 ')

for i in range(0,2):
    key[i] = float(key[i])

math(key[0],key[1])
print(math2(key[0],key[1]))
