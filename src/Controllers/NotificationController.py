from win10toast import ToastNotifier


class Notifier:
    def __init__(self, path_logo):
        self.toaster = ToastNotifier()
        self.logo = path_logo
        
        
    def exemplo(self):
        # exemplo
        toaster.show_toast(
            'Titulo',
            'Texto',
            threaded=True,
            icon_path=self.path_logo,
            duration=3
        )
    
    
    # Uma função para cada notificação


if __name__ == "__main__":
    path_logo = '../../assets/logo.png'
    notifier = Notifier()
    notifier.exemplo()

