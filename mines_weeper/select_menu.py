import pygame
import sys

pygame.init()

# Couleurs
DARK = (0, 0, 0)
BRUN = (200, 173, 127)

# Taille de la fenêtre
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu de Sélection de Difficulté")

# Police de texte
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def set_pseudo():
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color = color_inactive
    text_field = ''
    MAXIMUM_LENGTH = 12

    for event in pygame.event.get():
            if event.type != pygame.KEYDOWN:
                continue

            if pygame.K_a <= event.key <= pygame.K_z:
                if len(text_field) == MAXIMUM_LENGTH:
                    continue
                text_field = text_field + pygame.key.name(event.key)

            if event.key == pygame.K_BACKSPACE:
                text_field = text_field[:-1]

            # Dessine la zone de texte.
            pygame.draw.rect(screen, color, input_box, 2)
            font_surface = font.render(text_field, True, color)
            screen.blit(font_surface, (input_box.x + 5, input_box.y + 5))
            pygame.display.flip()

    return text_field

def affichage():
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
        # Chargement de l'image de fond
        image = pygame.image.load('1.png')
        scale = image.get_size()
        background_img = pygame.transform.scale(image , (400,400))

        # Chargement des images des boutons
        image = pygame.image.load('button.png')
        scale = image.get_size()
        button_img = pygame.transform.scale(image , (int(scale [0] * 2), int(scale [1]* 2)))

        #chargement de l'image de pseudo
        image = pygame.image.load('19.png')
        scale = image.get_size()
        pseudo_img = pygame.transform.scale(image , (int(scale [0] * 2), int (scale [1] * 2)))

        # Dessiner l'arrière-plan
        screen.fill(BRUN)
        screen.blit(background_img, (0, 0))

        # Dessiner les boutons
        easy_button_rect = button_img.get_rect(center=(WIDTH//2, HEIGHT//2 ))
        screen.blit(button_img, easy_button_rect)
        draw_text("Facile", font, DARK, screen, WIDTH//2, HEIGHT//2 )

        normal_button_rect = button_img.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
        screen.blit(button_img, normal_button_rect)
        draw_text("Normal", font, DARK, screen, WIDTH//2, HEIGHT//2 + 50)

        expert_button_rect = button_img.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
        screen.blit(button_img, expert_button_rect)
        draw_text("Expert", font, DARK, screen, WIDTH//2, HEIGHT//2 + 100)

        pseudo_init_rect = pseudo_img.get_rect(center=(WIDTH//2, HEIGHT//2 - 60))
        screen.blit(pseudo_img, pseudo_init_rect)
        draw_text("Entré votre pseudo :", font, DARK, screen, WIDTH//2, HEIGHT//2 - 120)

    
        # Mettre à jour l'affichage
        pygame.display.flip()


    





difficulty = affichage()
pseudo = set_pseudo()
print (pseudo)
print("Difficulté sélectionnée :", difficulty)
