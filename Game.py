import pygame 
import ClickableSprite
import Case as C
import Matrix
 
def on_left_click():
    sprite.image = pygame.image.load("empty.png").convert()

def on_right_click() :
    sprite.image = pygame.image.load("flag.png").convert()
 
matrix_size = 20

pygame.init()
screen = pygame.display.set_mode((matrix_size*32, matrix_size*32+64))

not_clicked = pygame.image.load("grid.png").convert()

sprite = ClickableSprite.ClickableSprite(not_clicked, 50, 50, on_left_click, on_right_click)

group = pygame.sprite.Group(sprite)
group.remove(sprite)


matrix = Matrix.Matrix((5, 10), matrix_size, group)

for i in range(matrix.get_matrix_size()) :
    for j in range(matrix.get_matrix_size()) :
        group.add(matrix.get_case((i,j)).get_sprite())

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or matrix.check_lose() or matrix.check_win():
            running = False

    group.update(events)
    screen.fill((255, 255, 255))
    group.draw(screen)
    pygame.display.update()
 
pygame.quit()