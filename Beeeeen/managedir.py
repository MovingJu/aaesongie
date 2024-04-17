import os
import time

def schndir():
    ndir = os.listdir()
    print('\n===== 현재 경로의 파일 =====\n')
    for i, j in enumerate(ndir):
        print(i+1, j)
    npath = os.getcwd()
    print(f'\n현재 경로 : {npath}\n')
    time.sleep(1)
    main()

def schddir():
    ddir_path = input('\n경로를 입력하세요 : ')
    ddir = os.listdir(ddir_path)
    print(f'\n===== 해당 경로의 파일 =====\n')
    for i, j in enumerate(ddir):
        print(i+1, j)
    print('\n')
    time.sleep(1)
    main()

def makedir():
    mkpath = input('\n경로를 입력하세요 : ')
    os.mkdir(mkpath)
    if os.path.exists(mkpath) == True:
        print('\n폴더가 생성되었습니다')
        time.sleep(1)
        main()
    else: print('\n폴더 생성에 실패했습니다')

def remodir():
    rmpath = input('\n경로를 입력하세요 : ')
    os.rmdir(rmpath)
    if os.path.exists(rmpath) == False:
        print('\n폴더가 삭제되었습니다')
        time.sleep(1)
        main()
    else: print('\n폴더 삭제에 실패했습니다')

def main():
    print('\n===== 어떤 작업을 수행하시겠습니까 =====\n')
    print('1. 현재 경로의 파일 확인')
    print('2. 특정 경로의 파일 확인')
    print('3. 특정 경로에 폴더 추가')
    print('4. 특정 경로의 폴더 제거')
    choice = input('\n작업을 선택하세요 (번호) : ')

    if choice == '1':
        schndir()
    elif choice == '2':
        schddir()
    elif choice == '3':
        makedir()
    elif choice == '4':
        remodir()
    else:
        print('\n!! 작업 번호를 입력해주세요')
        time.sleep(1)
        main()

if __name__ == '__main__':
    main()