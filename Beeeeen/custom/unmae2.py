zaeum_dict = {}

firfam = ['ㅂ','ㅃ','ㅍ','ㅁ']
secfam = ['ㄷ','ㄸ','ㅌ','ㅅ','ㅆ','ㄴ','ㄹ']
thifam = ['ㅈ','ㅉ','ㅊ']
forfam = ['ㄱ','ㄲ','ㅋ','ㅇ']
fiffam = ['ㅎ']
for i in range(len(firfam)):
    zaeum_dict[firfam[i]] = {'posi':'양순음'}
for i in range(len(secfam)):
    zaeum_dict[secfam[i]] = {'posi':'치조음'}
for i in range(len(thifam)):
    zaeum_dict[thifam[i]] = {'posi':'경구개음'}
for i in range(len(forfam)):
    zaeum_dict[forfam[i]] = {'posi':'연구개음'}
for i in range(len(fiffam)):
    zaeum_dict[fiffam[i]] = {'posi':'후음'}

onefam = ['ㅂ','ㅃ','ㅍ','ㄷ','ㄸ','ㅌ','ㄱ','ㄲ','ㅋ']
twofam = ['ㅈ','ㅉ','ㅊ']
thrfam = ['ㅅ','ㅆ','ㅎ']
foufam = ['ㅁ','ㄴ','ㅇ']
fivfam = ['ㄹ']

for i in range(len(onefam)):
    zaeum_dict[onefam[i]]['meth'] = '파열음'
for i in range(len(twofam)):
    zaeum_dict[twofam[i]]['meth'] = '파찰음'
for i in range(len(thrfam)):
    zaeum_dict[thrfam[i]]['meth'] = '마찰음'
for i in range(len(foufam)):
    zaeum_dict[foufam[i]]['meth'] = '비음'
for i in range(len(fivfam)):
    zaeum_dict[fivfam[i]]['meth'] = '유음'

hanfam = ['ㅂ','ㄷ','ㄱ','ㅈ','ㅅ']
dulfam = ['ㅃ','ㄸ','ㄲ','ㅉ','ㅆ']
setfam = ['ㅍ','ㅌ','ㅋ','ㅊ']
netfam = ['ㅎ','ㅁ','ㄴ','ㅇ','ㄹ']

for i in range(len(hanfam)):
    zaeum_dict[hanfam[i]]['meth2'] = '평음'
for i in range(len(dulfam)):
    zaeum_dict[dulfam[i]]['meth2'] = '경음'
for i in range(len(setfam)):
    zaeum_dict[setfam[i]]['meth2'] = '격음'
for i in range(len(netfam)):
    zaeum_dict[netfam[i]]['meth2'] = '없음'

def main():
    choicetable = {'자음' : zaserch,
                   '모음' : moserch}
    choice = input('\n무슨 음운을 검색하고 싶으신가요? : ')
    choicever = choicetable[choice]
    if choicever:
        choicever()

def zadir(x):
    print('\n===========================')
    print(f'\n검색하신 자음 : {x}')
    if zaeum_dict[x]['meth2'] == '없음':
        print(f'\n조음 위치 : {zaeum_dict[x]["posi"]}\n조음 방법 : {zaeum_dict[x]["meth"]}')        
    else:
        print(f'\n조음 위치 : {zaeum_dict[x]["posi"]}\n조음 방법 : {zaeum_dict[x]["meth"]},{zaeum_dict[x]["meth2"]}')
    print('\n===========================')

def modir(x):
    print(f'\n검색하신 모음 : {x}')
    print(f'\n조음 위치 : {zaeum_dict[x]["posi"]}\n조음 방법 : {zaeum_dict[x]["meth"]},{zaeum_dict[x]["meth2"]}')

def zaserch():
    search = input('무슨 자음을 검색하고 싶으신가요? : ')
    if search in zaeum_dict:
        zadir(search)
    else:
        print('자음만 입력해주세요!')
        zaserch()

def moserch():
    search = input('무슨 모음을 검색하고 싶으신가요? : ')
    if search in moeum_dict:
        modir(search)
    else:
        print('모음만 입력해주세요!')
        moserch()

if __name__ == '__main__':
    main()