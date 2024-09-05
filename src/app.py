import flet as ft
from config import Config
from Views import (
    LoginView, 
    SelectionView,
    AnimalRegisterView,
    AnimalRegisterResgateView,
    AdotanteRegisterView,
    AdotanteSearchView
)
from src.Views import SearchView


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
        self.page.add(ft.Text("Em Desenvolvimento"))
        if self.estado == "Login":
            LoginView.main(self.page, self)

        elif self.estado == "Tela Seleção":
            self.page.window_height = config.HEIGHT_BASE
            self.page.window_width = config.WIDTH_BASE
            SelectionView.main(self.page, self)

        elif self.estado == "Tela de Cadastro de Animal":
            self.page.window_height = config.HEIGHT_BASE * 1.5
            self.page.window_width = config.WIDTH_BASE * 1.2
            AnimalRegisterView.main(self.page)

        elif self.estado == "Tela de Cadastro de Resgate":
            self.page.window_height = config.HEIGHT_BASE
            self.page.window_width = config.WIDTH_BASE
            AnimalRegisterResgateView.main(self.page)

        elif self.estado == "Tela de Consulta de Animal":
            SearchView.main(self.page)

        elif self.estado == "Tela de Cadastro de Adotante":
            AdotanteRegisterView.main(self.page)

        # elif self.estado == "Tela de Consulta de Adotante":
        #     AdotanteSearchView.main(self.page)

        else:
            self.page.window_height = config.HEIGHT_LOGIN
            self.page.window_width = config.WIDTH_LOGIN
            LoginView.main(self.page, self)


ft.app(target=GerenciadorDeAnimaisAPAM)
