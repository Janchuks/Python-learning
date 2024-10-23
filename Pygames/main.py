import pygame
import random

pygame.init()
wx = 700
wy = 500
window = pygame.display.set_mode((wx, wy))
pygame.display.set_caption("COOKIE MONSTER")
pygame_icon = pygame.image.load('monster.png')
pygame.display.set_icon(pygame_icon)
running = True
monsterImg = pygame.image.load('monster.png')
MonsterX = 350
MonsterY = 250
cookie_original = pygame.image.load('cookie.png')

Cookie = pygame.transform.scale(cookie_original, (50, 50))
x = random.randint(0, 700)
y = random.randint(0, 500)

num = 0
MOnstrs = pygame.transform.scale(monsterImg, (50 + num, 50 + num))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if MonsterY - 0.3 >= 0:
                MonsterY -= 0.3
            else:
                MonsterY += 0
        if event.key == pygame.K_DOWN:
            if MonsterY + 0.3 <= 500 - 60:  # -60 jo monstra bildes garums
                MonsterY += 0.3
        if event.key == pygame.K_LEFT:
            if MonsterX - 0.3 >= 0:
                MonsterX -= 0.3
            else:
                MonsterX += 0
        if event.key == pygame.K_RIGHT:
            if MonsterX + 0.3 <= 700 - 60:  # -60 jo monstra bildes platums
                MonsterX += 0.3

        if MonsterX <= x + 50 and MonsterX + 50 >= x and MonsterY <= y + 50 and MonsterY + 50 >= y:
            x = random.randint(0, 650)
            y = random.randint(0, 450)
            MonsterX +=0.5
            MonsterY +=0.5
            num += 10
            MOnstrs = pygame.transform.scale(monsterImg, (50 + num, 50 + num))
        
    window.fill((0, 0, 0))
    window.blit(MOnstrs, (MonsterX, MonsterY))
    window.blit(Cookie, (x, y))
    pygame.display.update()
