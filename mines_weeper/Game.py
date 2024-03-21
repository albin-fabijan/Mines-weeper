import pygame 
import ClickableSprite as ClickableSprite
import Case as C
import Matrix as Matrix
 
def on_left_click():
    sprite.image = pygame.image.load("mines_weeper/sprites/empty.png").convert()

def on_right_click() :
    sprite.image = pygame.image.load("mines_weeper/sprites/flag.png").convert()

dif = 0
ok = False
while (not ok) :
    dif = int(input("difficulty (1-3) : "))
    if (not (dif < 1 or dif > 3)) :
        ok = True
    print(ok)

matrix_size = 20

pygame.init()
screen = pygame.display.set_mode((matrix_size*32, matrix_size*32+64))

not_clicked = pygame.image.load("mines_weeper/sprites/grid.png").convert()

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
        if event.type == pygame.QUIT:
            running = False
        if matrix.check_lose() :
            print("lose")
        if matrix.check_win() :
            print("win")


    group.update(events)
    screen.fill((255, 255, 255))
    group.draw(screen)
    pygame.display.update()
 
pygame.quit()