import pygame

def main():
    pygame.init()

    # Inizializza il modulo joystick
    pygame.joystick.init()

    # Controlla se ci sono joystick disponibili
    if pygame.joystick.get_count() == 0:
        print("Nessun joystick trovato. Assicurati che il controller Xbox 360 sia collegato.")
        return

    # Ottieni il primo joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Joystick connesso: {joystick.get_name()}")

    try:
        while True:
            # Gestisci gli eventi
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    print(f"Pulsante premuto: {event.button}")

    except KeyboardInterrupt:
        pass

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
