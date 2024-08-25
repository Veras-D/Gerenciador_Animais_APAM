import multiprocessing
import flet as ft


class PopupWindow:
    def __init__(self, page: ft.Page)
        self.page = page
        self.queue = multiprocessing.Queue()


    def create(self):
        def run_popup(self):
            ft.app(target=self.page)
        p2 = multiprocessing.Process(target=run_popup)
        p2.start()
        p2.join()

    
    def destroy(self):
        self.page_.window_destroy()
