import pygame
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("간단한 2D 게임")

# 색깔
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 캐릭터 설정
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT - player_height * 2
player_speed = 5

# 장애물 설정
enemy_width, enemy_height = 50, 50
enemy_x, enemy_y = random.randint(0, WIDTH - enemy_width), 0
enemy_speed = 3

# 게임 루프
run = True
while run:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # 장애물 이동
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_x, enemy_y = random.randint(0, WIDTH - enemy_width), 0
    
    # 충돌 체크
    if (player_x < enemy_x + enemy_width and
        player_x + player_width > enemy_x and
        player_y < enemy_y + enemy_height and
        player_y + player_height > enemy_y):
        print("게임 오버")
        run = False
    
    # 그리기
    win.fill(WHITE)
    pygame.draw.rect(win, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(win, BLUE, (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.display.update()

pygame.quit()
