import flet as ft
from config import Config
from Views import LoginView, SelectionView
from Controllers.LoginController import password_verification
# from util import Validacao
# from Models.Repository.db import DataBaseAPAM


config = Config()


class GerenciadorDeAnimaisAPAM:
    estado = "Login"
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = config.TITLE
        self.page.scroll = True
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_height = config.HEIGHT_LOGIN
        self.page.window_width = config.WIDTH_LOGIN
        self.main_page()


    def main_page(self):
        self.page.add(ft.Text("Teste"))
        if self.estado == "Login":
            LoginView.main(self.page, self)

        if self.estado == "Tela Seleção":
            self.page.window_height = config.HEIGHT_BASE
            self.page.window_width = config.WIDTH_BASE
            SelectionView.main(self.page)


ft.app(target=GerenciadorDeAnimaisAPAM)
