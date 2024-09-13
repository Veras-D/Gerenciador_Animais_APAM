import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import Models.Repository.db as database


db = database.DataBaseAPAM()
print(db.search_animal_or_adotante(target='adotante', search='ana'))


def search_animal(search: str = '') -> list:
    return db.search_animal_or_adotante(target='animal', search=search)


def search_adotante(search: str = '') -> list:
    return db.search_animal_or_adotante(target='adotante', search=search)


def main(page: ft.Page, estado=''):
    page.title = "Pesquisar Animal e Adotante"
    page.theme_mode = ft.ThemeMode.LIGHT

    pesquisa_animal=ft.Container(ft.Text("Pesq. Animal"))
    pesquisa_adotante=ft.Container(ft.Text("Pesq. Adotante"))


    def go_home(e):
        page.clean()
        estado.estado = "Tela Seleção"
        estado.main_page()


    icon_return = ft.Container(
        content=ft.IconButton(
            icon=ft.icons.HOME_OUTLINED,
            height=50,
            width=50,
            icon_color=ft.colors.BLACK
        ),
        padding=ft.padding.only(left=20),
        alignment=ft.alignment.center_left,
        on_click=go_home,
    )


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

    page.add(icon_return,
             t)


if __name__ == "__main__":
    ft.app(target=main)
