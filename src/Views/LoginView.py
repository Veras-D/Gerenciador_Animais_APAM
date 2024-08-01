import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from config import Config
from Controllers.LoginController import password_verification


config = Config()


def main(page, estado):

    page.title = config.TITLE
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = 'auto'

    user = ft.TextField(
        label='Nome de Usuário',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.BLACK, border_radius=10,
        autofocus=True
        )
    password = ft.TextField(
        label='Senha',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.BLACK, border_radius=10,
        password=True,
        can_reveal_password=True
        )
    logo_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'logo.png')

    def testar(e):
        print(user.value, password.value)
        print(type(user.value), type(password.value))
        if password_verification(page, user.value, password.value):
            page.clean()
            estado.estado = "Tela Seleção"
            estado.main_page()

    page.add(
        ft.Image(src=logo_path, width=120, height=120),
        ft.Container(height=20),
        ft.Row([
            ft.Column(
                [user,
                password,
                ft.ElevatedButton(text='Entrar', on_click=testar, width=300, height=40)],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
