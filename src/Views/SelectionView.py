import flet as ft

def main(page: ft.Page):
    page.title = "Tela de Seleção"
    page.bgcolor = "white" 

    def cadastrar_animal(e):
        ft.dialog("Ação", "Cadastrar Animal")

    def consultar_animal(e):
        ft.dialog("Ação", "Consultar Animal")

    def cadastrar_adotante(e):
        ft.dialog("Ação", "Cadastrar Adotante")

    def consultar_adotante(e):
        ft.dialog("Ação", "Consultar Adotante")

    button_style = ft.ButtonStyle(
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        shape=ft.RoundedRectangleBorder(radius=10),
        side=ft.BorderSide(width=2, color=ft.colors.BLACK),
        padding=10 
    )

    btn_cadastrar_animal = ft.OutlinedButton("Cadastrar Animal", on_click=cadastrar_animal, style=button_style, width=250, height=50)
    btn_consultar_animal = ft.OutlinedButton("Consultar Animal", on_click=consultar_animal, style=button_style,width=250, height=50)
    btn_cadastrar_adotante = ft.OutlinedButton("Cadastrar Adotante", on_click=cadastrar_adotante, style=button_style, width=250, height=50)
    btn_consultar_adotante = ft.OutlinedButton("Consultar Adotante", on_click=consultar_adotante, style=button_style, width=250, height=50)

    content = ft.Column(
        [
            btn_cadastrar_animal,
            btn_consultar_animal,
            btn_cadastrar_adotante,
            btn_consultar_adotante
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30,
        width=250
        
    )

    menu = ft.IconButton(
        icon=ft.icons.MENU,
        icon_color=ft.colors.BLACK,
        on_click=lambda e: print("Menu clicado"),
    )

    page.add(
        ft.Column(
            [
                ft.Row(
                    [menu],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Container(content, alignment=ft.alignment.center)
            ],
            expand=True
        )
    )

ft.app(target=main)
