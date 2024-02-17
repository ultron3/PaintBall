import os
import logging
import win10toast
class SaveManager:
    SAVE_FILE_NAME = 'D:\\BounceTale.mwc'

    @staticmethod
    def save_game_data():
        try:
            with open(SaveManager.SAVE_FILE_NAME, 'w') as file:
                file.write("Salvataggio effettuato\n")
            print("Salvataggio effettuato")
            #("Salvataggio effettuato"
            # )
            notification=win10toast.ToastNotifier()
            notification.show_toast("Salvataggio effettuato")
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")
            notification.show_toast(f"Errore durante il salvataggio: {e}")

    @staticmethod
    def check_storage_devices():
        available_drives = [drive for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{drive}:\\")]
        if available_drives:
            #print("Dispositivi di archiviazione trovati.")
            logging.info("Dispositivi di archiviazione trovati.")
            return True
        else:
            #print("Nessun dispositivo di archiviazione trovato.")
            logging.info("Nessun dispositivo di archiviazione trovato.")
            return False

# Esegui la verifica dei dispositivi di archiviazione all'avvio del gioco
if SaveManager.check_storage_devices():
    SaveManager.save_game_data()
