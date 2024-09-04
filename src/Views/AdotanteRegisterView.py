import flet as ft


def main(page, estado=''):
    page.title = "Cadastrar Adotante"
    page.theme_mode = ft.ThemeMode.LIGHT
    nome_adotante = ft.TextField(
        label="Nome Adotante",
        value="",
        width=650,
        height=56,
        border_radius=8,
    )

    referencia_rua = ft.TextField(
        hint_text="Referencia Rua",
        value="",
        width=320,
        border_radius=8,
        multiline=True,
        min_lines=7,
        max_lines=7,
    )

    cep_field = ft.TextField(
        label='CEP',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=270,
        color=ft.colors.WHITE,
        border_radius=10
    )

    cep_icon = ft.IconButton(
        icon=ft.icons.LOCATION_ON_OUTLINED,
        icon_color=ft.colors.BLACK,
        height=50,
        width=50,
        # on_click=pass
    )

    rua_field = ft.TextField(
        hint_text='Rua',
        read_only=True,
        focused_border_color=ft.colors.BLACK,
        value='',
        width=210,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
    )

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
        alignment=ft.alignment.center_left,
        on_click=go_home,
    )

    area_localizacao = ft.Column([
        ft.Row([
            cep_field,
            cep_icon,
        ]),
        rua_field,
    ])

    container_loc = ft.Container(
                content=area_localizacao,
                padding=10,
                border_radius=10,
                bgcolor='#DEE4F8',
                height=360,
                width=400,
    )

    page.add(
        icon_return,
        ft.Column([
            ft.Row([nome_adotante, container_loc])
        ]),
    )



if __name__ == "__main__":
    ft.app(target=main)
