import pygame


class Window:
    def __init__(self, WIDTH, HEIGHT):
        pygame.init()

        self.running = True

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Menu de Sélection de Difficulté")

        self.font = pygame.font.Font(None, 36)

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)


