import unittest
import xml.etree.ElementTree as ET
import pygame
import sys
import os
# Aggiungi il percorso della cartella principale al percorso di ricerca dei moduli
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("C:\\Users\\IdeaPad\\OneDrive\\Documenti\\PaintBall\\UnitTest\\testXbox.py"), '..')))
import xboxController as np
class TestXboxController(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.xbox_controller = np.XboxController(joystick_index=0)  # Assumi che la classe XboxController sia stata implementata

    def tearDown(self):
        pygame.quit()

    def test_get_input(self):
        input_values = self.xbox_controller.get_input()

        # Esempio: Verifica che i valori dell'input siano compresi in un certo intervallo
        self.assertTrue(-1 <= input_values[0] <= 1, "Valore X del joystick sinistro fuori intervallo")
        self.assertTrue(-1 <= input_values[1] <= 1, "Valore Y del joystick sinistro fuori intervallo")
        self.assertTrue(-1 <= input_values[2] <= 1, "Valore X del joystick destro fuori intervallo")
        self.assertTrue(-1 <= input_values[3] <= 1, "Valore Y del joystick destro fuori intervallo")
        # Aggiungi altre asserzioni in base alle tue esigenze

    def test_generate_xml(self):
        input_values = self.xbox_controller.get_input()

        # Crea un elemento radice XML
        root = ET.Element("ControllerProperties")

        # Aggiungi sottoelementi per ogni proprietà del controller
        ET.SubElement(root, "LeftStickX").text = str(input_values[0])
        ET.SubElement(root, "LeftStickY").text = str(input_values[1])
        ET.SubElement(root, "RightStickX").text = str(input_values[2])
        ET.SubElement(root, "RightStickY").text = str(input_values[3])

        # Aggiungi sottoelementi per ciascun pulsante
        buttons_element = ET.SubElement(root, "Buttons")
        for i, button_state in enumerate(input_values[4]):
            ET.SubElement(buttons_element, f"Button_{i}").text = str(button_state)

        # Crea un oggetto ElementTree e scrivi il risultato su un file XML
        tree = ET.ElementTree(root)
        tree.write("C:\\GameMultiPlatform\\SetupController\\xbox_controller_properties.xml")

if __name__ == "__main__":
    unittest.main()
