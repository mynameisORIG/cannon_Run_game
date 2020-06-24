#!/usr/bin/python3

# libraries
import pygame, sys, random
from functionAndClasses import GameVariables, Link, enemy, detect_collision, drop_enemies, draw_enemies ,updateEnemyPos, collision_check, Winner

#you have to initialize pygame first
pygame.init()

pygame.display.set_caption("Link's endless enemies")

# variables
player_pos = [650, 370, 50]
enemy_pos1 = [55, 400]
enemy_pos2 = [55, 500]
enemy_pos3 = [55, 300]
enemy_list1 = [enemy_pos1]
delay = random.random()

screen = pygame.display.set_mode((GameVariables.WIDTH, GameVariables.HEIGHT))

while not GameVariables.game_over:

    for event in pygame.event.get():
        # print event location
        #print(event)

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= Link.player_step
            elif event.key == pygame.K_RIGHT:
                x += Link.player_step
            elif event.key == pygame.K_UP:
                y -= Link.player_step
            elif event.key == pygame.K_DOWN:
                y += Link.player_step 
            player_pos = [x,y, 50]

        screen.blit(GameVariables.bg, (0,0))

        if player_pos[0] > GameVariables.WIDTH or player_pos[0] < 0:
            sys.exit()
        elif  player_pos[1] > 275 and player_pos[0] < 55:
            Winner()
        # Update Position of enemy
        #enemy3
        if enemy_pos3[0] >= 0 and enemy_pos3[0] < GameVariables.HEIGHT:
            enemy_pos3[0] += GameVariables.speed 
        else:
            enemy_pos3[0] = random.randint(0, GameVariables.WIDTH-enemy.enemy_size)
            enemy_pos3[0] = 0
        if detect_collision(player_pos,enemy_pos3):
            GameVariables.game_over = True
        #enemy2
        if enemy_pos2[0] >= 0 and enemy_pos2[0] < GameVariables.HEIGHT:
            enemy_pos2[0] += GameVariables.speed
        else:
            enemy_pos2[0] = random.randint(0, GameVariables.WIDTH-enemy.enemy_size)
            enemy_pos2[0] = 0
        if detect_collision(player_pos, enemy_pos2):
            GameVariables.game_over = True

        # borders
        if player_pos[1] <= 220:
            player_pos = [650, 370, 50]
        elif player_pos[1] >=  510 :
            player_pos = [650, 370, 50]
        
        drop_enemies(enemy_list1)
        updateEnemyPos(enemy_list1)
        if collision_check(enemy_list1, player_pos):
            GameVariables.game_over = True
            break
        draw_enemies(enemy_list1)
        pygame.draw.circle(screen, enemy.black, (enemy_pos2[0], enemy_pos2[1]) , 20 )
        pygame.draw.circle(screen, enemy.black, (enemy_pos3[0], enemy_pos3[1]) , 20 )
        screen.blit(enemy.cannon, (55, 475, 0, 0))
        screen.blit(enemy.cannon, (55, 375, 0, 0))
        screen.blit(enemy.cannon, (55, 275, 0, 0))
        screen.blit(Link.LOZ_Link, (player_pos[0], player_pos[1], player_pos[2], player_pos[2]))
        GameVariables.clock.tick(30)
        
        pygame.display.update()


