import pygame 
import ClickableSprite
import Case as C
import Matrix
 
def on_left_click():
    sprite.image = pygame.image.load("empty.png").convert()

def on_right_click() :
    sprite.image = pygame.image.load("flag.png").convert()
 
pygame.init()
screen = pygame.display.set_mode((20*32, 20*32))

not_clicked = pygame.image.load("grid.png").convert()

#case_1 = Case.Case(False, (0,0))
#case0 = Case.Case(True, (0,1), num_bombs=0)
#case1 = Case.Case(True, (0,2), num_bombs=1)
sprite = ClickableSprite.ClickableSprite(not_clicked, 50, 50, on_left_click, on_right_click)

#group = pygame.sprite.GroupSingle(sprite)
#group = pygame.sprite.Group(case_1.get_sprite())
#group.add(case0.get_sprite())
#group.add(case1.get_sprite())


group = pygame.sprite.Group(sprite)
group.remove(sprite)


matrix = Matrix.Matrix((5, 10), 20, group)

for i in range(matrix.get_matrix_size()) :
    for j in range(matrix.get_matrix_size()) :
        group.add(matrix.get_case((i,j)).get_sprite())

# matrix.show()

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