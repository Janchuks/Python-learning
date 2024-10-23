import pygame

pygame.init()

window = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Catch all the cookies!")
icon = pygame.image.load('monster.png')
pygame.display.set_icon(icon)

monsterImg = pygame.image.load('monster.png')
monsterX = 350
monsterY = 250
monsterY_change = 0
monsterX_change = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                monsterX += 0.3
            if event.key == pygame.K_a:
                monsterX -= 0.3
            if event.key == pygame.K_s:
                monsterY += 0.3
            if event.key == pygame.K_w:
                monsterY -= 0.3


    monsterX += monsterX_change
    monsterY += monsterY_change

    window.fill((0, 0, 0)) #rgb - redgreenblue
    window.blit(monsterImg, (monsterX, monsterY))
    pygame.display.update()