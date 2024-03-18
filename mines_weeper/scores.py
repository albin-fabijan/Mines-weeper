import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Affichage des Scores")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRUN = (200, 173, 127)

# Police de texte
font = pygame.font.SysFont(None, 40)

def afficher_score(timer, niveau, result):

    # Chargement de l'image de fond
    screen.fill(BRUN)
    background_img = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\1.png')
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Chargement de l'image du bouton
    button_img = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\button.png')
    button_img = pygame.transform.scale(button_img, (450, 100))

    # Affichage du score sur l'image du bouton
    text_score = font.render(f"Votre timer: {timer}", True, BLACK)
    score_rect = text_score.get_rect(center=(button_img.get_width() // 2, button_img.get_height() // 2))
    button_img.blit(text_score, score_rect)

    # Affichage des éléments
    screen.blit(background_img, (0, 0))  # Affichage de l'image de fond
    screen.blit(button_img, (SCREEN_WIDTH // 2 - button_img.get_width() // 2, 50))



    pygame.draw.rect(screen, BLACK, (50, 500, 200, 50))  # Bouton recommencer
    pygame.draw.rect(screen, BLACK, (550, 500, 200, 50))  # Bouton quitter

    text_recommencer = font.render("Recommencer", True, WHITE)
    text_quitter = font.render("Quitter", True, WHITE)

    screen.blit(text_recommencer, (65, 515))
    screen.blit(text_quitter, (575, 515))

    pygame.display.flip()



def main():
    timer = 60  # Exemple de timer
    niveau = 1  # Exemple de niveau de difficulté
    result = True #exemple de resultat

     # Chargement de l'image de fond
    image = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\1.png')
    scale = image.get_size()
    background_img = pygame.transform.scale(image , (350,350))

    # Chargement des images des boutons
    image = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\button.png')
    scale = image.get_size()
    button_img = pygame.transform.scale(image , (int(scale [0] * 2), int(scale [1]* 2)))

    afficher_score(timer, niveau , result)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 50 <= mouse_pos[0] <= 250 and 500 <= mouse_pos[1] <= 550:
                    print("Recommencer")
                    # Ajouter ici le code pour recommencer
                elif 550 <= mouse_pos[0] <= 750 and 500 <= mouse_pos[1] <= 550:
                    print("Quitter")
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
