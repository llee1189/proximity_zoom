import pygame
import socket

pygame.init()

# Display and Background
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Proximity Zoom")
background = pygame.image.load('house.png')
stairs = pygame.image.load('stairs.png')
middle = pygame.image.load('middle_walls.png')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player
playerIcon = pygame.image.load('player.png')
# player = pygame.transform.scale(player, (32, 32))
pX = 768
pY = 200
display.blit(playerIcon, (pX, pY))
pX_change = 0
pY_change = 0
up = False
down = False
left = False
right = False
sprint = False
playerRect = pygame.Rect(pX, pY, 32, 32)

walls = []
walls.append(pygame.Rect(375, 0, 51, 80))
walls.append(pygame.Rect(376, 177, 212, 63))
walls.append(pygame.Rect(241, 249, 406, 103))
walls.append(pygame.Rect(724, 249, 76, 103))
walls.append(pygame.Rect(0, 249, 164, 103))
walls.append(pygame.Rect(366, 442, 49, 158))
walls.append(pygame.Rect(0, 0, 63, 184))
walls.append(pygame.Rect(64, 0, 219, 89))
walls.append(pygame.Rect(29, 431, 46, 98))
# top_wall = pygame.Rect(375, 0, 51, 80)
# stair_wall = pygame.Rect(376, 177, 212, 63)
# middle_wall = pygame.Rect(241, 249, 406, 103)
# right_wall = pygame.Rect(724, 249, 76, 103)
# left_wall = pygame.Rect(0, 249, 164, 103)
# bottom_wall = pygame.Rect(366, 442, 49, 158)
# left_counter = pygame.Rect(0, 0, 63, 184)
# top_counter = pygame.Rect(64, 0, 219, 89)
# television = pygame.Rect(29, 431, 46, 98)



tempest = pygame.display.get_surface()


def player(x, y):
    display.blit(playerIcon, (x, y))
    playerRect.x = x
    playerRect.y = y


def collision(wall):
    global pX
    global pY

    if pX > wall.x - 32 > pX - 5:
        pX = wall.x - 32
    if pX < wall.x + wall.size[0] < pX + 5:
        pX = wall.x + wall.size[0]
    if pY < wall.y + wall.size[1] < pY + 5:
        pY = wall.y + wall.size[1]
    if pY > wall.y - 32 > pY - 5:
        pY = wall.y - 32


running = True

while running:
    display.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        k = pygame.key.get_mods()
        if k == 4097:
            sprint = True
        else:
            sprint = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pX_change = -1
                left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pX_change = 1
                right = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                pY_change = -1
                up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                pY_change = 1
                down = True

        if event.type == pygame.KEYUP:
            # LEFT
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and right:
                pX_change = 1
                left = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pX_change = 0.0
                left = False
            # RIGHT
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and left:
                pX_change = -1
                right = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pX_change = 0.0
                right = False
            # UP
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and down:
                pY_change = 1
                up = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                pY_change = 0.0
                up = False
            # DOWN
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and up:
                pY_change = -1
                down = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                pY_change = 0.0
                down = False
    if sprint:
        pX += pX_change * 2
        pY += pY_change * 2
    else:
        pX += pX_change
        pY += pY_change
    if pX < 0:
        pX = 0
    elif pX > 768:
        pX = 768
    if pY < 0:
        pY = 0
    elif pY > 568:
        pY = 568

    for wall in walls:
        if wall.colliderect(playerRect):
            collision(wall)
    # if top_wall.colliderect(playerRect):
    #     collision(top_wall)
    #
    # if stair_wall.colliderect(playerRect):
    #     collision(stair_wall)
    #
    # if middle_wall.colliderect(playerRect):
    #     collision(middle_wall)
    #
    # if right_wall.colliderect(playerRect):
    #     collision(right_wall)
    #
    # if left_wall.colliderect(playerRect):
    #     collision(left_wall)
    #
    # if bottom_wall.colliderect(playerRect):
    #     collision(bottom_wall)
    #
    # if left_counter.colliderect(playerRect):
    #     collision(left_counter)
    #
    # if top_counter.colliderect(playerRect):
    #     collision(top_counter)
    #
    # if television.colliderect(playerRect):
    #     collision(television)

    # pygame.draw.rect(tempest, (0, 0, 255, 255), right_wall)
    player(pX, pY)
    display.blit(stairs, (83, -121))
    display.blit(middle, (0, 0))
    pygame.display.update()
