import flet as ft


def main(page):
    page.title = "Tela de Seleção"
    page.bgcolor = "white"


    button_style = ft.ButtonStyle(
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        shape=ft.RoundedRectangleBorder(radius=10),
        side=ft.BorderSide(width=2, color=ft.colors.BLACK),
        padding=10 
    )

    btn_cadastrar_animal = ft.OutlinedButton("Cadastrar Animal", on_click='', style=button_style, width=250, height=50)
    btn_consultar_animal = ft.OutlinedButton("Consultar Animal", on_click='', style=button_style,width=250, height=50)
    btn_cadastrar_adotante = ft.OutlinedButton("Cadastrar Adotante", on_click='', style=button_style, width=250, height=50)
    btn_consultar_adotante = ft.OutlinedButton("Consultar Adotante", on_click='', style=button_style, width=250, height=50)

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

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Image(src="assets/logo.png", width=150, height=150),
            ft.Container(height=20),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="Home",
                icon=ft.icons.HOME,
                selected_icon_content=ft.Icon(ft.icons.HOME),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.INFO),
                label="Logs",
                selected_icon=ft.Icon(ft.icons.INFO),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PEOPLE),
                label="About Us",
                selected_icon=ft.icons.PEOPLE,
            ),
            ft.Divider(thickness=2)
        ],
    )

    def menu(e):
        page.drawer.open = True
        page.drawer.update()

    menu = ft.IconButton(
        icon=ft.icons.MENU,
        icon_color=ft.colors.BLACK,
        on_click=menu,
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
            # expand=True  # Não descomente isso, se não o app.py não funciona
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
