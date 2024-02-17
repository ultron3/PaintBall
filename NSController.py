import pygame

class NSController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def get_input(self):
        pygame.event.pump()

        left_stick_x = self.controller.get_axis(0)
        left_stick_y = self.controller.get_axis(1)

        return left_stick_x, left_stick_y

    def close(self):
        pygame.quit()
