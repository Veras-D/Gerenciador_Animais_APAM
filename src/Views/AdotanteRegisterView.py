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

    profissao_adotante = ft.TextField(
        label="Nome Adotante",
        value="",
        width=210,
        height=56,
        border_radius=8,
    )

    rg_adotante = ft.TextField(
        label="RG",
        value="",
        width=210,
        height=56,
        border_radius=8,
    )

    cpf_adotante = ft.TextField(
        label="CPF",
        value="",
        width=210,
        height=56,
        border_radius=8,
    )

    email_adotante = ft.TextField(
        label="Email",
        value="",
        width=430,
        height=56,
        border_radius=8,
    )

    complemento_adotante = ft.Dropdown(
        width=210,
        hint_text="Complemento",
        options=[
            ft.dropdown.Option("Apartamento"),
            ft.dropdown.Option("Bloco"),
            ft.dropdown.Option("Sala"),
            ft.dropdown.Option("Andar"),
            ft.dropdown.Option("Lote"),
            ft.dropdown.Option("Condomínio"),
            ft.dropdown.Option("Casa"),
            ft.dropdown.Option("Quadra"),
        ],
        border_radius=8
    )

    telefone_fixo_adotante = ft.TextField(
        label="Telefone Fixo",
        value="",
        width=210,
        height=56,
        border_radius=8,
    )

    telefone_celular_adotante = ft.TextField(
        label="Telefone Celular",
        value="",
        width=210,
        height=56,
        border_radius=8,
    )

    referencia_rua = ft.TextField(
        hint_text="Referencia Rua",
        value="",
        width=650,
        border_radius=8,
        multiline=True,
        min_lines=7,
        max_lines=7,
    )

    cep_field = ft.TextField(
        label='CEP',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=230,
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
        width=300,
        # text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
    )

    num_field = ft.TextField(
        label='Numero',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        # text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
    )

    bairo_field = ft.TextField(
        hint_text='Bairo',
        read_only=True,
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        # text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
    )

    cidade_field = ft.TextField(
        hint_text='Cidade',
        read_only=True,
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        # text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
    )

    uf_field = ft.TextField(
        hint_text='UF',
        read_only=True,
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        # text_align=ft.TextAlign.CENTER,
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
            ft.Container(content=cep_icon, border=ft.border.all(1, ft.colors.BLACK), border_radius=10),
        ]),
        rua_field,
        num_field,
        bairo_field,
        cidade_field,
        uf_field,
    ])

    container_loc = ft.Container(
                content=area_localizacao,
                padding=20,
                border_radius=20,
                bgcolor='#DEE4F8',
                height=430,
                width=340,
    )
    fields = ft.Column([
        nome_adotante,
        ft.Row([
            profissao_adotante,
            rg_adotante,
            cpf_adotante,
        ]),
        ft.Row([
            email_adotante,
            complemento_adotante,

        ]),
        ft.Row([
            telefone_fixo_adotante,
            telefone_celular_adotante,
        ]),
        referencia_rua,
    ])

    submit_button = ft.ElevatedButton(
        text="Salvar",
        # on_click=save_func,
        color=ft.colors.BLACK
    )

    page.add(
        icon_return,
        ft.Column([
            ft.Row([ft.Container(content=fields, padding=50), container_loc])
        ]),
        ft.Container(
            content=submit_button,
            alignment=ft.alignment.bottom_right,
            padding=ft.padding.only(right=20, bottom=20)
        ),
    )



if __name__ == "__main__":
    ft.app(target=main)
