import pygame

# Inizializza Pygame
pygame.init()

# Inizializza il controller
controller = pygame.joystick.Joystick(0)
controller.init()
try:
# Ciclo principale
    while True:
    # Gestisci eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # Leggi input dal controller
    # Puoi personalizzare questa parte in base alle tue esigenze
            left_stick_x = controller.get_axis(0)
            left_stick_y = controller.get_axis(1)
            right_stick_x = controller.get_axis(2)
            right_stick_y = controller.get_axis(3)

            buttons = [controller.get_button(i) for i in range(controller.get_numbuttons())]

    # Stampa i valori dell'input
            print(f"Left Stick: ({left_stick_x}, {left_stick_y})")
            print(f"Right Stick: ({right_stick_x}, {right_stick_y})")
            print(f"Buttons: {buttons}")

    # Aggiorna la finestra di Pygame (non necessario se non stai usando la finestra)
            pygame.display.update()
except pygame.error as e:
    print(e)