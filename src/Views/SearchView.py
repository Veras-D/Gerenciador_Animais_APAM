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
                    print(len(container_animal.controls))
                    dados_animal = db.get_animais(id_animal=valor_pesquisa[1])[0]
                    try:
                        dados_castracao = db.get_castracao(id_animal=valor_pesquisa[1])[0]
                        castrado = "Sim"
                        data_castracao = dados_castracao[2]
                    except IndexError:
                        castrado = "Não"
                        data_castracao = "Não Castrado"
                    # print(dados_castracao)
                    if len(container_animal.controls) >= 3:
                        container_animal.controls.pop()


                    # Erro grave, não é possível prosseguir
                    conteudo_animal = ft.Column([
                        ft.Text(f"Perfil Animal {valor_pesquisa[0]}", size=20, weight=ft.FontWeight.BOLD),
                        ft.Row([
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(ft.Text("Nome")),
                                    ft.DataColumn(ft.Text("Especie")),
                                    ft.DataColumn(ft.Text("Gênero")),
                                    ft.DataColumn(ft.Text("Temperamento")),
                                    ft.DataColumn(ft.Text("Idade")),
                                    ft.DataColumn(ft.Text("Porte")),
                                    ft.DataColumn(ft.Text("Raça")),
                                    ft.DataColumn(ft.Text("Microchip")),
                                    ft.DataColumn(ft.Text("Status")),
                                    ft.DataColumn(ft.Text("Possui Sequela")),
                                ],
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text(f"{dados_animal[2]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[3]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[4]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[5]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[6]} {dados_animal[7]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[8]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[10]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[11]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[12]}")),
                                            ft.DataCell(ft.Text(f"{dados_animal[13]}")),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Text(f"Pelagem: {dados_animal[9]}"),
                        ft.Text("Observações"),
                        ft.TextField(
                            value=dados_animal[14],
                            multiline=True,
                            read_only=True,
                            min_lines=7, max_lines=7,
                        ),
                        ft.Text(f"Dados de Castração Animal {valor_pesquisa[0]}", size=20, weight=ft.FontWeight.BOLD),
                        ft.Row([
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(ft.Text("É Castrado")),
                                    ft.DataColumn(ft.Text("Data Castração")),
                                ],
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text(f"{castrado}")),
                                            ft.DataCell(ft.Text(f"{data_castracao}")),
                                        ]
                                    )
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Text("Animal"),
                    ])

                    perfil = ft.Container(
                        conteudo_animal,
                    )

                    container_animal.controls.append(perfil)
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
        anchor_adotante.controls = [
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
                    print(len(page.controls))
                    if len(page.controls) >= 3:
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
             t,
    )


if __name__ == "__main__":
    ft.app(target=main)
