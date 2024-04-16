import random

# 3x3 크기의 빈 게임판 생성
game_board = [[" " for _ in range(3)] for _ in range(3)]

# 게임판 출력 함수
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# 초기 게임판 출력
print_board(game_board)

# 플레이어의 입력 받기
def get_player_move():
    while True:
        move = input("어디에 플레이하시겠어요? (예: 행,열) ")
        try:
            row, col = map(int, move.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1  # 리스트 인덱스는 0부터 시작하므로 1을 빼줍니다.
            else:
                print("잘못된 위치입니다. 다시 입력해주세요.")
        except ValueError:
            print("입력 형식이 잘못되었습니다. 다시 입력해주세요.")

# 플레이어의 마크로 해당 위치에 표시하기
def make_move(board, row, col, mark):
    if board[row][col] == " ":
        board[row][col] = mark
        return True
    else:
        print("이미 다른 플레이어가 선택한 위치입니다.")
        return False

# 게임판을 출력하고 플레이어의 입력을 받아서 표시하기
def play(board, mark):
    print_board(board)
    while True:
        row, col = get_player_move()
        if make_move(board, row, col, mark):
            break

# 게임 시작
play(game_board, "X")

# 컴퓨터의 랜덤 플레이
def computer_play(board, mark):
    print("컴퓨터의 차례입니다.")
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if make_move(board, row, col, mark):
            break

# 게임 종료 여부 확인
def is_game_over(board):
    # 가로, 세로, 대각선에 같은 마크가 3개 연속으로 있는지 확인
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    # 모든 셀이 채워져 있는지 확인 (무승부 조건)
    for row in board:
        if " " in row:
            return False
    return True

# 게임 시작
while True:
    play(game_board, "X")  # 플레이어의 차례
    if is_game_over(game_board):
        break

    computer_play(game_board, "O")  # 컴퓨터의 차례
    if is_game_over(game_board):
        break

print_board(game_board)
print("게임 종료!")
