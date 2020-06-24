#!/usr/bin/python3
import pygame, sys, random


# classes
class GameVariables:
    WIDTH = 800
    HEIGHT = 600
    game_over = False
    bg = pygame.image.load('./images/backgroundImage.png')
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    speed = 10

class Link:
    LOZ_Link = pygame.image.load('./images/pixel_LOZ_link.png')
    player_step = 40
    LOZ_Link = pygame.transform.scale(LOZ_Link, (125, 75))

class enemy:
    cannon = pygame.image.load('./images/cannon.png')
    cannon = pygame.transform.scale(cannon, (125,75))
    black = (0,0,0)
    enemy_size = 50

# functions

screen = pygame.display.set_mode((GameVariables.WIDTH, GameVariables.HEIGHT))

def detect_collision(player_pos, enemy_pos1):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos1[0]
    e_y = enemy_pos1[1]

    if (e_x >= p_x and e_x < (p_x + 50)) or (p_x >= e_x and (p_x < e_x+enemy.enemy_size)):
        if (e_y >= p_y and e_y < (p_y + 50)) or (p_y >= e_y and p_y < (e_y+enemy.enemy_size)):
            return True
    return False

def drop_enemies(enemy_list1):
    delay = random.random()
    if len(enemy_list1) < 2 and delay < 0.1:
        x_pos = random.randint(0, GameVariables.WIDTH-enemy.enemy_size)
        y_pos = 400
        enemy_list1.append([x_pos, y_pos])

def draw_enemies(enemy_list1):
    for enemy_pos1 in enemy_list1:
        pygame.draw.circle(screen, enemy.black, (enemy_pos1[0], enemy_pos1[1]) , 20 )

def updateEnemyPos(enemy_list1):
   #enemy1
    for idx, enemy_pos1 in enumerate(enemy_list1):
        if enemy_pos1[0] >= 0 and enemy_pos1[0] < GameVariables.HEIGHT:
            enemy_pos1[0] += GameVariables.speed
        else:
            #enemy_pos1[0] = random.randint(0, GameVariables.WIDTH-enemy.enemy_size)
            #enemy_pos1[0] = 0
            enemy_list1.pop(idx)
            
def collision_check(enemy_list1, player_pos):
    for enemy_pos1 in enemy_list1:
        if enemy_pos1[0] >= 0 and enemy_pos1[0] < GameVariables.HEIGHT:
            enemy_pos1[0] += GameVariables.speed
        else:
            enemy_pos1[0] = random.randint(0, GameVariables.WIDTH-enemy.enemy_size)
            enemy_pos1[0] = 0
        if detect_collision(player_pos,enemy_pos1):
            GameVariables.game_over = True
def Winner():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    done = False

    font = pygame.font.SysFont("Bauhaus 93", 72)

    text = font.render("You Win!!!!!", True, (0, 128, 0))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        
        screen.fill((255, 255, 255))
        screen.blit(text,
            (320 - text.get_width() // 2, 240 - text.get_height() // 2))
        
        pygame.display.flip()
        clock.tick(60)
    sys.exit() 