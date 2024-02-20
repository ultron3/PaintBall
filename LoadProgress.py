import win10toast

class LoadManager:
    SAVE_FILE_NAME = 'D:\\BounceTale.DAT'

    @staticmethod
    def load_game_data():
        try:
            with open(LoadManager.SAVE_FILE_NAME, 'r') as file:
                data = file.read()
                print("Dati del gioco caricati:", data)
                notification = win10toast.ToastNotifier()
                notification.show_toast("Dati del gioco caricati", data)
        except Exception as e:
            print(f"Errore durante il caricamento: {e}")
            notification.show_toast(f"Errore durante il caricamento: {e}")

# Esegui il caricamento dei dati del gioco
LoadManager.load_game_data()

