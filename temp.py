import flet as ft


def main(page: ft.Page, estado=''):
    page.title = "Cadastrar Adotante"
    page.theme_mode = ft.ThemeMode.LIGHT

    pesquisa_animal=ft.Container(ft.Text("Pesq. Animal"))
    pesquisa_adotante=ft.Container(ft.Text("Pesq. Adotante"))

    t = ft.Tabs(
        animation_duration=300,
        tab_alignment=ft.TabAlignment.CENTER,
        tabs=[
            ft.Tab(
                text="Consultar Animal",
                content=ft.Container(
                    content=pesquisa_animal
                ),
            ),
            ft.Tab(
                text="Consultar Adotante",
                content=pesquisa_adotante
            ),
        ],
        # expand=1,
    )

    page.add(t)

ft.app(main)
