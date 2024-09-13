import flet as ft
import src.Models.Repository.db as database


db = database.DataBaseAPAM()

def search_animal(search: str = '') -> list:
    return db.search_animal_or_adotante(target='animal', search=search)


def search_adotante(search: str = '') -> list:
    return db.search_animal_or_adotante(target='adotante', search=search)


def main(page):
    page.scroll = "always"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    pesq = db.search_animal_or_adotante()


    def close_anchor(e):
        text = e.control.data
        print(f"closing view from {text}")
        anchor.close_view(text)


    def handle_change(e):
        pesq = db.search_animal_or_adotante(search=e.data)
        print(f"handle_change e.data: {e.data}")
        anchor.controls = [
            ft.ListTile(title=ft.Text(i[0]), on_click=close_anchor, data=i)
            for i in pesq
        ]
        anchor.update()


    page.snack_bar = ft.SnackBar(
        content=ft.Text("Pesquisa Invalida!", color=ft.colors.WHITE),
        bgcolor=ft.colors.RED,
    )


    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")
        valor_pesquisa = e.data[1:-1].replace(' ', '').split(',')
        if len(valor_pesquisa) == 2 and valor_pesquisa[1]:
            try:
                valor_pesquisa[1] = int(valor_pesquisa[1])
            except ValueError:
                valor_pesquisa[1] = ''
            finally:
                if not valor_pesquisa[1]:
                    page.snack_bar.open = True
                else:
                    # Verrifcar depois de o numero de elementos não mudou
                    print(len(page.controls))
                    if len(page.controls) >= 2:
                        page.controls.pop()
                    perfil = ft.Container()
                    page.controls.append(perfil)
                    page.update()

    def handle_tap(e):
        print(f"handle_tap")
        anchor.open_view()


    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Procurar animal...",
        view_hint_text="Procure pelo nome do animal...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            ft.ListTile(title=ft.Text(i[0]), on_click=close_anchor, data=i)
            for i in pesq
        ],
    )


    page.add(
        # ft.Row(
        #     alignment=ft.MainAxisAlignment.CENTER,
        #     controls=[
        #         ft.OutlinedButton(
        #             "Open Search View",
        #             on_click=lambda _: anchor.open_view(),
        #         ),
        #     ],
        # ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[anchor],
        )
    )


ft.app(main)
