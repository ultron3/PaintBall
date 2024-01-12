import pygame

class PSController:
    def __init__(self, joystick_index=0):
        pygame.init()
        self.controller = pygame.joystick.Joystick(joystick_index)
        self.controller.init()

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        left_stick_x = self.controller.get_axis(0)
        left_stick_y = self.controller.get_axis(1)
        right_stick_x = self.controller.get_axis(2)
        right_stick_y = self.controller.get_axis(3)

        # Modifica il mapping dei pulsanti per il controller PlayStation
        # Questo è solo un esempio, potrebbe variare a seconda del tuo controller
        square_button = self.controller.get_button(0)
        cross_button = self.controller.get_button(1)
        circle_button = self.controller.get_button(2)
        triangle_button = self.controller.get_button(3)

        buttons = [square_button, cross_button, circle_button, triangle_button]

        return left_stick_x, left_stick_y, right_stick_x, right_stick_y, buttons

def main():
    ps_controller = PSController()
    try:
        while True:
            input_values = ps_controller.get_input()

            # Stampa i valori dell'input
            print(f"Left Stick: ({input_values[0]}, {input_values[1]})")
            print(f"Right Stick: ({input_values[2]}, {input_values[3]})")
            print(f"Buttons: {input_values[4]}")

            pygame.display.update()
    except pygame.error as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
