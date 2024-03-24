import pygame

class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, left_click, right_click):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left_click = left_click
        self.right_click = right_click
 
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.left_click()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.rect.collidepoint(event.pos):
                    self.right_click()
