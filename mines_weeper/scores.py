import pygame
import sys
import json

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Affichage des Scores")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRUN = (200, 173, 127)
BEIGE = (63, 34, 4)

# Police de texte
font = pygame.font.SysFont(None, 40)

def afficher_score(timer):
    # Chargement de l'image de fond
    screen.fill(BRUN)
    background_img = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\1.png')
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Chargement de l'image du score
    button_img = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\button.png')
    button_img = pygame.transform.scale(button_img, (450, 100))

    # Affichage du score
    text_score = font.render(f"Votre timer: {timer}", True, BLACK)
    score_rect = text_score.get_rect(center=(button_img.get_width() // 2, button_img.get_height() // 2))
    button_img.blit(text_score, score_rect)

    # Affichage des boutons
    screen.blit(background_img, (0, 0))  # Affichage de l'image de fond
    screen.blit(button_img, (SCREEN_WIDTH // 2 - button_img.get_width() // 2, 50))

    # Affichage du bouton "Recommencer" avec le texte
    restart_button_img = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\select.png')
    restart_button_img = pygame.transform.scale(restart_button_img, (200, 100))
    restart_text = font.render("Recommencer", True, BEIGE)
    restart_rect = restart_text.get_rect(center=(restart_button_img.get_width() // 2, restart_button_img.get_height() // 2))
    restart_button_img.blit(restart_text, restart_rect)
    screen.blit(restart_button_img, (SCREEN_WIDTH - 250, SCREEN_HEIGHT - 150))

    # Affichage du bouton "Quitter" avec le texte
    quit_button_img = pygame.image.load('C:\\Users\\étude\\Documents\\Mines-weeper\\mines_weeper\\select.png')
    quit_button_img = pygame.transform.scale(quit_button_img, (200, 100))
    quit_text = font.render("Quitter", True, BEIGE)
    quit_rect = quit_text.get_rect(center=(quit_button_img.get_width() // 2, quit_button_img.get_height() // 2))
    quit_button_img.blit(quit_text, quit_rect)
    screen.blit(quit_button_img, (50, SCREEN_HEIGHT - 150))

    pygame.display.flip()

def afficher_resultat_et_niveau(result, niveau):
    result_text = "Gagné !" if result else "Perdu..."
    if niveau == 1:
        niveau_text = f"difficulté: facile"
    elif niveau == 2:
        niveau_text = f"difficulté: normale"
    elif niveau == 3:
        niveau_text = f"difficulté: difficile"
    
    result_font = pygame.font.SysFont(None, 60)
    result_surface = result_font.render(result_text, True, BLACK)
    result_rect = result_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

    niveau_font = pygame.font.SysFont(None, 40)
    niveau_surface = niveau_font.render(niveau_text, True, BLACK)
    niveau_rect = niveau_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    
    screen.blit(result_surface, result_rect)
    screen.blit(niveau_surface, niveau_rect)
    pygame.display.flip()

def main():
    timer = 60  # Exemple de timer
    niveau = 1  # Exemple de niveau de difficulté
    result = True  # Exemple de resultat

    afficher_score(timer)
    
    afficher_resultat_et_niveau(result, niveau)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 50 <= mouse_pos[0] <= 250 and SCREEN_HEIGHT - 150 <= mouse_pos[1] <= SCREEN_HEIGHT - 50:
                    print("Quitter")
                    pygame.quit()
                    sys.exit()
                elif SCREEN_WIDTH - 250 <= mouse_pos[0] <= SCREEN_WIDTH - 50 and SCREEN_HEIGHT - 150 <= mouse_pos[1] <= SCREEN_HEIGHT - 50:
                    print("Recommencer")
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
