import pygame
import sys
import time
import logging
import xboxController as np
import PlaystationController as ps
# Configurazione del modulo di logging
logging.basicConfig(filename='game_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
pygame.init()
# Carica il file audio in formato MP3
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\IdeaPad\\OneDrive\\Documenti\PaintBall\\FileAudioPaintBall.mpeg')
#background_image = pygame.image.load('C:\\Users\\IdeaPad\\OneDrive\\Documenti\\PaintBall\\sfondogame.jpeg')  # Sostituisci 'path/to/background_image.jpg' con il percorso del tuo file immagine
#background_rect = background_image.get_rect()

# Riproduci la musica in loop (-1 indica la riproduzione continua)
pygame.mixer.music.play(-1)

# Tentativo di inizializzazione del controller Xbox
try:
    platform_controller = np.XboxController(0)
    #print("Xbox controller detected.")
    logging.info("Xbox controller detected.")
except Exception as xbox_error:
    # Se si verifica un'eccezione, potrebbe essere perché il controller Xbox non è connesso
    #print("Xbox controller not detected:", xbox_error)
    logging.warning("Xbox controller not detected:", xbox_error)

    # Tentativo di inizializzazione del controller PlayStation
    try:
        platform_controller = ps.PSController(0)
        #print("PlayStation controller detected.")
        logging.info("Playstation controller detected.")
    except Exception as ps_error:
        # Se neanche il controller PlayStation è connesso, potrebbe essere un problema
        print("PlayStation controller not detected:", ps_error)
        logging.warning("Xbox controller not detected:", ps_error)
        raise RuntimeError("Nessun controller rilevato. Assicurati che almeno un controller sia collegato.")
background_image = pygame.image.load('C:\\Users\\IdeaPad\\OneDrive\\Documenti\\PaintBall\\sfondogame.jpeg')
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gioco con Salto e Punteggio")
background_image = pygame.transform.scale(background_image, (width, height))
white = (255, 255, 255)
red = (255, 0, 0)

player_x, player_y = width // 2, height // 2
player_radius = 20
player_speed = 5

# Variabili per il salto
is_jumping = True
jump_count = 10

# Variabile per il punteggio
score = 0
font = pygame.font.Font(None, 36)

# Funzione per disegnare il punteggio
def draw_score():
    try:
        score_text = font.render("Punteggio: {}".format(score), True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
    except Exception as e:
        logging.warning(f"error {e}")

# Inizializza il joystick
try:
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    
    if joystick_count > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick_name = joystick.get_name()
        logging.info(f"joistick trovato {joystick_name}")
    else:
        print("Nessun joystick trovato.")
        logging.warning("Nessun joystick trovato.")
except pygame.error as e:
    logging.error(f"error: {e}")
try:
    start_screen_image = pygame.image.load('C:\\Users\\IdeaPad\\OneDrive\\Documenti\\PaintBall\\sfondogame.jpeg')  # Sostituisci con il percorso del tuo file immagine
    start_screen_image = pygame.transform.scale(start_screen_image, (width, height))

    # Visualizza l'immagine di avvio per 3 secondi
    start_screen_duration = 3  # Tempo in secondi
    start_screen_start_time = time.time()

    while time.time() - start_screen_start_time < start_screen_duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    screen.blit(start_screen_image, (0, 0))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    # Resetta il timer
    start_screen_start_time = time.time()
except:
    logging("image not found")
# Effetto di inizio gioco
start_effect_frames = 60  # Numero di frame per l'effetto di inizio
start_effect_countdown = start_effect_frames
try:
    while start_effect_countdown > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()# Interrompi la musica prima di uscire
              
                pygame.quit()
                sys.exit()

    # Disegna la finestra di gioco durante l'effetto di inizio
        screen.fill(white)
        pygame.draw.circle(screen, red, (int(player_x), int(player_y)), player_radius)
        draw_score()

    # Aggiorna la finestra di gioco
        pygame.display.flip()

        start_effect_countdown -= 1
        pygame.time.Clock().tick(60)
except pygame.error as e:
    logging.error(f"error:{e}")
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    screen.blit(background_image, (0, 0))

    # Logica del salto
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Muovi il giocatore con il joystick
    if joystick_count > 0:
        player_x += joystick.get_axis(0) * player_speed
        player_y += joystick.get_axis(1) * player_speed

    # Impedisci che la pallina esca dagli schermi orizzontali
    player_x = max(player_radius, min(player_x, width - player_radius))

    # Impedisci che la pallina esca dagli schermi verticali
    player_y = max(player_radius, min(player_y, height - player_radius))

    # Disegna la finestra di gioco
    screen.fill(white)
    pygame.draw.circle(screen, red, (int(player_x), int(player_y)), player_radius)
    draw_score()
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Controlla gli eventi dei pulsanti del joystick
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # Puoi adattare i numeri dei pulsanti in base al tuo joystick
            # Logica per far esplodere la pallina
                    logging.info("Il pulsante è stato premuto! La pallina esplode!")
            # Puoi aggiungere qui la logica per far esplodere la pallina, ad esempio resettare la posizione o fare qualche animazione
    except pygame.error as e:
        logging.error(f"error:{e}")
    # Verifica se il punteggio ha raggiunto o superato 1000
    if joystick_count > 0:  
        if score < 1000:
        # Incrementa il punteggio solo se è inferiore a 1000
            score += 1
            #logging.info(f"the score max is: {score}")

    # Aggiorna la finestra di gioco
    pygame.display.flip()

    # Imposta il numero di frame al secondo
    pygame.time.Clock().tick(60)
    

