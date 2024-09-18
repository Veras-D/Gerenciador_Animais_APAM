import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import Models.Repository.db as database


db = database.DataBaseAPAM()


def main(page: ft.Page, estado=''):
    page.title = "Pesquisar Animal e Adotante"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "always"
    pesq_animal = db.search_animal_or_adotante()
    pesq_adotante = db.search_animal_or_adotante(target='adotante')


    def close_anchor_animal(e):
        text = e.control.data
        print(f"closing view from {text}")
        anchor_animal.close_view(text)


    def handle_change_animal(e):
        pesq = db.search_animal_or_adotante(search=e.data)
        print(f"handle_change e.data: {e.data}")
        anchor_animal.controls = [
            ft.ListTile(title=ft.Text(i[0]), on_click=close_anchor_animal, data=i)
            for i in pesq
        ]
        anchor_animal.update()


    page.snack_bar_animal = ft.SnackBar(
        content=ft.Text("Pesquisa Invalida!", color=ft.colors.WHITE),
        bgcolor=ft.colors.RED,
    )


    def handle_submit_animal(e):
        print(f"handle_submit e.data: {e.data}")
        valor_pesquisa = e.data[1:-1].replace(' ', '').split(',')
        if len(valor_pesquisa) == 2 and valor_pesquisa[1]:
            try:
                valor_pesquisa[1] = int(valor_pesquisa[1])
            except ValueError:
                valor_pesquisa[1] = ''
            finally:
                if not valor_pesquisa[1]:
                    page.snack_bar_animal.open = True
                else:
                    # Verrifcar depois de o numero de elementos não mudou
                    print(len(page.controls))
                    if len(page.controls) >= 2:
                        page.controls.pop()
                    perfil = ft.Container()
                    page.controls.append(perfil)
                    page.update()

    def handle_tap_animal(e):
        print(f"handle_tap")
        anchor_animal.open_view()


    anchor_animal = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Procurar animal...",
        view_hint_text="Procure pelo nome do animal...",
        on_change=handle_change_animal,
        on_submit=handle_submit_animal,
        on_tap=handle_tap_animal,
        controls=[
            ft.ListTile(title=ft.Text(i[0]), on_click=close_anchor_animal, data=i)
            for i in pesq_animal
        ],
    )


    def close_anchor_adotante(e):
        text = e.control.data
        print(f"closing view from {text}")
        anchor_adotante.close_view(text)


    def handle_change_adotante(e):
        pesq = db.search_animal_or_adotante(search=e.data)
        print(f"handle_change e.data: {e.data}")
        anchor_adotate.controls = [
            ft.ListTile(title=ft.Text(i[0]), on_click=close_anchor_adotante, data=i)
            for i in pesq
        ]
        anchor_adotante.update()


    page.snack_bar_adotante = ft.SnackBar(
        content=ft.Text("Pesquisa Invalida!", color=ft.colors.WHITE),
        bgcolor=ft.colors.RED,
    )


    def handle_submit_adotante(e):
        print(f"handle_submit e.data: {e.data}")
        valor_pesquisa = e.data[1:-1].replace(' ', '').split(',')
        if len(valor_pesquisa) == 2 and valor_pesquisa[1]:
            try:
                valor_pesquisa[1] = int(valor_pesquisa[1])
            except ValueError:
                valor_pesquisa[1] = ''
            finally:
                if not valor_pesquisa[1]:
                    page.snack_bar_adotante.open = True
                else:
                    # Verrifcar depois de o numero de elementos não mudou
                    print(len(page.controls))
                    if len(page.controls) >= 2:
                        page.controls.pop()
                    perfil = ft.Container()
                    page.controls.append(perfil)
                    page.update()

    def handle_tap_adotante(e):
        print(f"handle_tap")
        anchor_adotante.open_view()


    anchor_adotante = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Procurar adotante...",
        view_hint_text="Procure pelo nome do adotante...",
        on_change=handle_change_adotante,
        on_submit=handle_submit_adotante,
        on_tap=handle_tap_adotante,
        controls=[
            ft.ListTile(title=ft.Text(i[0]), on_click=close_anchor_adotante, data=i)
            for i in pesq_adotante
        ],
    )

    container_animal = ft.Column([
        ft.Container(height=10),
        ft.Row([anchor_animal],
        alignment=ft.MainAxisAlignment.CENTER
        ),
    ])
    
    container_adotante = ft.Column([
        ft.Container(height=10),
        ft.Row([anchor_adotante],
        alignment=ft.MainAxisAlignment.CENTER
        ),
    ])
    pesquisa_animal=ft.Container(container_animal)
    pesquisa_adotante=ft.Container(container_adotante)


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
