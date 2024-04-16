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
'''
for i in range(1,101):
    for j in range(1,101):
        m = i*j
        print(f'print({i}*{j})={m}')
