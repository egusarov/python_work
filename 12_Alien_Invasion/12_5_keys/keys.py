import pygame


pygame.init()
screen = pygame.display.set_mode((400, 240))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(event.key)

pygame.quit()