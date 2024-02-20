from SaveProgres import SaveManager
import win10toast
import sys
import os


class LoadManager(SaveManager):
    @staticmethod
    def load_game_data():
        try:
            with open(LoadManager.SAVE_FILE_NAME, 'r') as file:
                data = file.read()
                print("Dati del gioco caricati:", data)
         
                
        except Exception as e:
            print(f"Errore durante il caricamento: {e}")
            

# Esegui il caricamento dei dati del gioco
LoadManager.load_game_data()
