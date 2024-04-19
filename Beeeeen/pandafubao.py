import sys
import time
import pandas as pd
import matplotlib.pyplot as plt

def main():
    mainprint = ['데이터 확인하기',
                 '데이터 수정하기',
                 '데이터 시각화하기',
                 '종료']
    print('\n===== 데이터 작업 =====\n')
    for i, j in enumerate(mainprint, start=1):
        print(f'{i}. {j}')
    
    mainselect = {'1' : func1,
                  '2' : func2,
                  '3' : func3,
                  '4' : sys.exit}
    select = input('\n어떤 작업을 하시겠어요? : ')
    selected = mainselect[select]
    if selected:
        selected()
    else:
        print('\n나열된 작업의 번호만 입력하세요')
        time.sleep(1)
        main()

def func1():
    typetable = {'csv' : pd.read_csv,
                 'xlsx' : pd.read_excel}
    seetable = {''}
    datatype = input('\n데이터의 종류를 입력하세요 : ')
    selectedtype = typetable[datatype]
    if selectedtype:
        func1path()
    else:
        print('현재 csv와 xlsx만 지원합니다')
        func1()

def func1path():
    datapath = input('데이터의 경로를 입력하세요 : ')
    print()
    dataseme = input('확인 방식을 선택하세요 : ')
    df = selectedtype(datapath)
    print(df)

def func2():
    ''
def func3():
    ''

if __name__ == '__main__':
    main()