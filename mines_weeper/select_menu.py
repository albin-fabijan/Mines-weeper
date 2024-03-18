import pygame
import sys

pygame.init()

# Couleurs
DARK = (0, 0, 0)
BRUN = (200, 173, 127)

# Taille de la fenêtre
WIDTH, HEIGHT = 350, 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu de Sélection de Difficulté")

# Police de texte
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main():

    # Chargement de l'image de fond
    image = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\1.png')
    scale = image.get_size()
    background_img = pygame.transform.scale(image , (350,350))

    # Chargement des images des boutons
    image = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\button.png')
    scale = image.get_size()
    button_img = pygame.transform.scale(image , (int(scale [0] * 2), int(scale [1]* 2)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Récupérer les coordonnées de la souris au moment du clic
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Vérifier si le clic est sur un des boutons
                if easy_button_rect.collidepoint(mouse_x, mouse_y):
                    return 1
                elif normal_button_rect.collidepoint(mouse_x, mouse_y):
                    return 2
                elif expert_button_rect.collidepoint(mouse_x, mouse_y):
                    return 3

        # Dessiner l'arrière-plan
        screen.fill(BRUN)
        screen.blit(background_img, (0, 0))

        # Dessiner les boutons
        easy_button_rect = button_img.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        screen.blit(button_img, easy_button_rect)
        draw_text("Facile", font, DARK, screen, WIDTH//2, HEIGHT//2 - 50)

        normal_button_rect = button_img.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(button_img, normal_button_rect)
        draw_text("Normal", font, DARK, screen, WIDTH//2, HEIGHT//2)

        expert_button_rect = button_img.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
        screen.blit(button_img, expert_button_rect)
        draw_text("Expert", font, DARK, screen, WIDTH//2, HEIGHT//2 + 50)

        # Mettre à jour l'affichage
        pygame.display.flip()

if __name__ == "__main__":
    difficulty = main()
    print("Difficulté sélectionnée :", difficulty)
