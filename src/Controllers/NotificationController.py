from win10toast import ToastNotifier


class Notifier:
    def __init__(self, path_logo):
        self.toaster = ToastNotifier()
        self.logo = path_logo
        
        
    def exemplo(self):
        # exemplo
        self.toaster.show_toast(
            'Titulo',
            'Texto',
            threaded=True,
            icon_path=self.logo,
            duration=3
        )
    
    
    # Uma função para cada notificação


if __name__ == "__main__":
    path_logo = '../../assets/logo.png'
    notifier = Notifier(path_logo)
    notifier.exemplo()
