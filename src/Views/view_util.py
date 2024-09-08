import multiprocessing
import flet as ft


class PopupWindow:
    def __init__(self, page: ft.Page):
        self.page = page
        self.queue = multiprocessing.Queue()
        def run_popup(self):
            ft.app(target=self.page)
        self.p2 = multiprocessing.Process(target=run_popup)


    def create(self):
        self.p2.start()
        self.p2.join()


    def destroy(self):
        self.page.window_destroy()
        self.p2.terminate()
