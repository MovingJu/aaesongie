import os

def read_diary():
    if os.path.exists("diary.txt"):
        with open("diary.txt", "r", encoding="utf-8") as file:
            diary_content = file.read()
            print("=== 내 일기 ===")
            print(diary_content)
    else:
        print("일기가 존재하지 않습니다.")

def write_diary():
    print("일기를 작성하세요 (종료하려면 '종료' 입력):")
    diary_content = []
    while True:
        line = input()
        if line == "종료":
            break
        diary_content.append(line)
    
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write("\n".join(diary_content)+"\n")
    print("일기를 저장했습니다.")

def trash_diary():
    with open("diary.txt", "w", encoding="utf-8") as file:
        file.write("")
    print("일기를 초기화했습니다.")

def main():
    while True:
        print("1. 일기 작성하기")
        print("2. 일기 읽기")
        print("3. 종료")
        print("4. 일기 초기화")              # 내가 한번 추가해본다
        choice = input("메뉴를 선택하세요: ")
        
        if choice == "1":
            write_diary()
        elif choice == "2":
            read_diary()
        elif choice == "3":
            print("일기장을 종료합니다.")
            break
        elif choice == "4":
            trash_diary()
        else:
            print("올바른 메뉴 번호를 입력하세요.")

if __name__ == "__main__":
    main()
