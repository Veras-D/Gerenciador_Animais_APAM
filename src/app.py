import flet as ft
import config
from util import Validacao
from Models.Repository.db import DataBaseAPAM


class GerenciadorDeAnimaisAPAM:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.INDIGO_900
        self.page.title = "Gerenciador de Animais | ASSOCIAÇÃO MATO-GROSSENSE PROTETORA DOS ANIMAIS (APAM)"
        self.page.scroll = True
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.main_page()


    def main_page(self):
        self.page.add(ft.Text("Teste"))


ft.app(target=GerenciadorDeAnimaisAPAM)

