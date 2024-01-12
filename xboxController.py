import pygame
import logging
class XboxController:
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

        buttons = [self.controller.get_button(i) for i in range(self.controller.get_numbuttons())]

        return left_stick_x, left_stick_y, right_stick_x, right_stick_y, buttons


def main():
    xbox_controller = XboxController()
    logging.basicConfig(filename='controller.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        while True:
            input_values = xbox_controller.get_input()

        # Stampa i valori dell'input
            print(f"Left Stick: ({input_values[0]}, {input_values[1]})")
            print(f"Right Stick: ({input_values[2]}, {input_values[3]})")
            print(f"Buttons: {input_values[4]}")
            
            logging.info(f"Left Stick: ({input_values[0]}, {input_values[1]})")
            logging.info(f"Left Stick: ({input_values[0]}, {input_values[1]})")
            logging.info(f"Buttons: {input_values[4]}")

            pygame.display.update()
    except pygame.error as e:
        print(e)

if __name__ == "__main__":
    main()
