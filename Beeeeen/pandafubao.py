import sys
import time
import pandas as pd
import os
import matplotlib.pyplot as plt

def main():
    mainprint = ['데이터 확인하기',
                 '데이터 수정하기',
                 '데이터 시각화하기',
                 '종료']
    print('\n======== 데이터 작업 ========\n')
    for i, j in enumerate(mainprint, start=1):
        print(f'{i}. {j}')
    mainselect = {'1' : func1,
                  '2' : func2,
                  '3' : func3,
                  '4' : sys.exit}
    select = input('\n어떤 작업을 하시겠어요? : ')
    selected = mainselect.get(select)
    if selected:
        selected()
    else:
        print('\n나열된 작업의 번호만 입력하세요')
        time.sleep(1)
        main()

def func1():
    typetable = {'csv' : pd.read_csv,
                 'xlsx' : pd.read_excel}
    print()
    for i in typetable:
        print(f'{i}')
    datatype = input('\n데이터의 종류를 입력하세요 : ')
    selectedtype = typetable.get(datatype)
    if selectedtype:
        func1path(selectedtype)
    else:
        print('\n현재 csv와 xlsx만 지원합니다')
        time.sleep(1)
        func1()

def func1path(x):
    datapath = input('데이터의 경로를 입력하세요 : ')
    if os.path.exists(datapath):
        df = x(datapath)
        func1see(df)
    else:
        print('정확한 경로를 입력해주세요')
        func1path(x)

def func1see(x):
    time.sleep(1)
    fucn1see = ['all',
                'head',
                'tail',
                'iloc',
                'info']
    print()
    for i in fucn1see:
        print(f'{i}')
    dataseme = input('\n확인 방식을 선택하세요 : ')
    if dataseme == 'all':
        print(x)
        restart()
    elif dataseme == 'head':
        print(x.head(5))
        restart()
    elif dataseme == 'tail':
        print(x.tail(5))
        restart()
    elif dataseme == 'iloc':
        print(x.iloc[5:10, :])
        restart()
    elif dataseme == 'info':
        print(x.info())
        restart()
    else:
        print('나열된 작업 중 선택해주세요')
        time.sleep(1)
        func1see()

def func2():
    ''
def func3():
    ''
def func4():
    ''

def restart():
    outtable = {'y' : main,
                'n' : sys.exit}
    time.sleep(2)
    logout = input('\n메뉴로 돌아가시겠어요? (y/n) : ')
    selectedout = outtable.get(logout)
    if selectedout:
        selectedout()
    else:
        print('나열된 작업 중 선택해주세요')
        restart()

if __name__ == '__main__':
    main()