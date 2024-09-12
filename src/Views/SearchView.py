import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import Models.Repository.db as database


banco = database.DataBaseAPAM()
print(banco.search_animal_or_adotante(target='adotante', search='ana'))


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


if __name__ == "__main__":
    ft.app(target=main)
