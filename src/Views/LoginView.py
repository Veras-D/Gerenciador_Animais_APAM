import flet as ft

def main(page: ft.Page):

    page.title="ASSOCIAÇÃO MATO-GROSSENSE PROTETORA DOS ANIMAIS (APAM)"
    page.bgcolor=ft.colors.INDIGO_900
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_height = 400
    page.window_width = 400
    page.scroll = 'auto'

    user = ft.TextField(
        label='Nome de Usuário',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.WHITE, border_radius=10,
        autofocus=True
        )
    password = ft.TextField(
        label='Senha',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.WHITE, border_radius=10,
        password=True,
        can_reveal_password=True
        )

    page.add(
        ft.Image(src="assets/logo.png", width=120, height=120),
        ft.Container(height=20),
        ft.Row([
            ft.Column(
                [user,
                password,
                ft.ElevatedButton(text='Entrar', on_click='', width=300, height=40, color=ft.colors.WHITE)],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
