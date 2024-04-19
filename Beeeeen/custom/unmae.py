import time

class Unmae:
    def __init__(self, visual, mksposi, mksmeth1, mksmeth2):
        self.visual = visual
        self.mksposi = mksposi
        self.mksmeth1 = mksmeth1
        self.mksmeth2 = mksmeth2

ㄱ = Unmae(visual="ㄱ", mksposi="연구개음", mksmeth1="파열음", mksmeth2="평음")
ㄲ = Unmae(visual="ㄲ", mksposi="연구개음", mksmeth1="파열음", mksmeth2="경음")
ㅋ = Unmae(visual="ㅋ", mksposi="연구개음", mksmeth1="파열음", mksmeth2="격음")
ㄴ = Unmae(visual="ㄴ", mksposi="치조음", mksmeth1="비음", mksmeth2="")
ㄷ = Unmae(visual="ㄷ", mksposi="치조음", mksmeth1="파열음", mksmeth2="평음")
ㄸ = Unmae(visual="ㄸ", mksposi="치조음", mksmeth1="파열음", mksmeth2="경음")
ㅌ = Unmae(visual="ㅌ", mksposi="치조음", mksmeth1="파열음", mksmeth2="격음")
ㄹ = Unmae(visual="ㄹ", mksposi="치조음", mksmeth1="유음", mksmeth2="")
ㅁ = Unmae(visual="ㅁ", mksposi="양순음", mksmeth1="비음", mksmeth2="")
ㅂ = Unmae(visual="ㅂ", mksposi="양순음", mksmeth1="파열음", mksmeth2="평음")
ㅃ = Unmae(visual="ㅃ", mksposi="양순음", mksmeth1="파열음", mksmeth2="경음")
ㅍ = Unmae(visual="ㅍ", mksposi="양순음", mksmeth1="파열음", mksmeth2="격음")
ㅅ = Unmae(visual="ㅅ", mksposi="치조음", mksmeth1="마찰음", mksmeth2="평음")
ㅆ = Unmae(visual="ㅆ", mksposi="치조음", mksmeth1="마찰음", mksmeth2="경음")
ㅇ = Unmae(visual="ㅇ", mksposi="연구개음", mksmeth1="비음", mksmeth2="")
ㅈ = Unmae(visual="ㅈ", mksposi="경구개음", mksmeth1="파찰음", mksmeth2="평음")
ㅉ = Unmae(visual="ㅉ", mksposi="경구개음", mksmeth1="파찰음", mksmeth2="경음")
ㅊ = Unmae(visual="ㅊ", mksposi="경구개음", mksmeth1="파찰음", mksmeth2="격음")
ㅎ = Unmae(visual="ㅎ", mksposi="후음", mksmeth1="마찰음", mksmeth2="")

def zadir(x):
    print(f'\n검색하신 자음 : {x.visual}')
    print(f'\n조음 위치 : {x.mksposi}\n조음 방법 : {x.mksmeth1}-{x.mksmeth2}')

def zaserch():
    search = input('무슨 자음을 검색하고 싶으신가요? : ')
    if search == 'ㄱ':
        zadir(ㄱ)
    elif search == 'ㄲ':
        zadir(ㄲ)
    elif search == 'ㅋ':
        zadir(ㅋ)
    elif search == 'ㄴ':
        zadir(ㄴ)
    elif search == 'ㄷ':
        zadir(ㄷ)
    elif search == 'ㄸ':
        zadir(ㄸ)
    elif search == 'ㅌ':
        zadir(ㅌ)
    elif search == 'ㄹ':
        zadir(ㄹ)
    elif search == 'ㅁ':
        zadir(ㅁ)
    elif search == 'ㅂ':
        zadir(ㅂ)
    elif search == 'ㅃ':
        zadir(ㅃ)
    elif search == 'ㅍ':
        zadir(ㅍ)
    elif search == 'ㅅ':
        zadir(ㅅ)
    elif search == 'ㅆ':
        zadir(ㅆ)
    elif search == 'ㅇ':
        zadir(ㅇ)
    elif search == 'ㅈ':
        zadir(ㅈ)
    elif search == 'ㅉ':
        zadir(ㅉ)
    elif search == 'ㅊ':
        zadir(ㅊ)
    elif search == 'ㅎ':
        zadir(ㅎ)
    else:
        print('자음만 입력해주세요!')
        zaserch()
zaserch()