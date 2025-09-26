import pygame, sys

# init
pygame.init()
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x, y = 200, 200
dx, dy = 20, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: dx, dy = 0, -20
    if keys[pygame.K_DOWN]: dx, dy = 0, 20
    if keys[pygame.K_LEFT]: dx, dy = -20, 0
    if keys[pygame.K_RIGHT]: dx, dy = 20, 0

    x = (x + dx) % WIDTH
    y = (y + dy) % HEIGHT

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, 20, 20))
    pygame.display.flip()
    clock.tick(10)
