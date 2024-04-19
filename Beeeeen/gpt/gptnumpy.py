import numpy as np
import keyboard
import os
import time

# 화면 크기 설정
WIDTH, HEIGHT = 93, 31
player_x, player_y = WIDTH // 2, HEIGHT - 1
enemy_x, enemy_y = np.random.randint(0, WIDTH), 0
player_char = 'P'
enemy_char = 'E'
empty_char = ' '

# 게임 루프
while True:
    # 게임 화면 초기화
    game_screen = np.full((HEIGHT, WIDTH), empty_char)
    game_screen[player_y, player_x] = player_char
    game_screen[enemy_y, enemy_x] = enemy_char

    # 게임 화면 출력
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in game_screen:
        print(' '.join(row))

    # 장애물 이동
    enemy_y += 1
    if enemy_y >= HEIGHT:
        enemy_x, enemy_y = np.random.randint(0, WIDTH), 0

    # 키 입력 처리
    if keyboard.is_pressed('a') and player_x > 0:
        player_x -= 1
    if keyboard.is_pressed('d') and player_x < WIDTH - 1:
        player_x += 1

    # 충돌 검사
    if player_x == enemy_x and player_y == enemy_y:
        print("게임 오버!")
        break

    # 게임 속도 조절
    time.sleep(0.1)
