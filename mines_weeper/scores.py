import pygame
import sys

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

def afficher_score(timer, niveau, result, pseudo ):
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

    # Affichage du pseudo
    if pseudo == False:
        text_pseudo = font.render("Entrée votre pseudo." , True , BLACK)
        pseudo_rect = text_pseudo.get_rect(center=(button_img.get_width(), button_img.get_height()))
        button_img.blit(text_pseudo,pseudo_rect)
    else:
        text_pseudo = font.render(f"Pseudo: {pseudo}", True, BLACK)
        pseudo_rect = text_pseudo.get_rect(center=(button_img.get_width() // 2, button_img.get_height() // 4))
        button_img.blit(text_pseudo, pseudo_rect)


    pygame.display.flip()

def saisir_pseudo():
    pseudo = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return pseudo
                elif event.key == pygame.K_BACKSPACE:
                    pseudo = pseudo[:-1]
                else:
                    pseudo += event.unicode

def main():
    timer = 60  # Exemple de timer
    niveau = 1  # Exemple de niveau de difficulté
    result = True  # Exemple de resultat
    pseudo = False
    

    afficher_score(timer, niveau, result , pseudo )

    pseudo = saisir_pseudo()

    afficher_score(timer, niveau, result , pseudo)


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
