import pygame
import sprite
import grid

window = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
running = True
tictactoe = grid.Grid()

while running:
    time_delta = clock.tick(60)
    window.fill([100,0,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tictactoe.show(window)
    tictactoe.place(window)
    pygame.display.update()
