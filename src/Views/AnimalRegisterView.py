import flet as ft
import datetime
import multiprocessing
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import Models.Repository.db as database
import Models.Entities.animal as animal
import util


q = multiprocessing.Queue(maxsize=1)
db = database.DataBaseAPAM()


class Page2(ft.Page):
    def __init__(self):
        super().__init__()


def popup(page_: Page2):
    page_.title = "CheckBox Pelagem"
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page_.window_width = 400
    page_.window_height = 420
    # page_.window_resizable = False
    page_.theme_mode = ft.ThemeMode.LIGHT
    page_.scroll = True
    
    
    def button_clicked(e):
        list_values = {
            f"{c1.label}": c1.value,
            f"{c2.label}": c2.value,
            f"{c3.label}": c3.value,
            f"{c4.label}": c4.value,
            f"{c5.label}": c5.value,
            f"{c6.label}": c6.value,
            f"{c7.label}": c7.value,
            f"{c8.label}": c8.value,
            f"{c9.label}": c9.value,
            f"{c10.label}": c10.value,
            f"{c11.label}": c11.value,
            f"{c12.label}": c12.value,
            f"{c13.label}": c13.value,
            f"{c14.label}": c14.value,
        }

        pelagens = [chave for chave, valor in list_values.items() if valor]
        q.put(pelagens)

        print(list_values)
        print(pelagens)
        # print(q.get())
        page_.window_destroy()
    
    t = ft.Text(value="Escolha a Palagem do Protegido", size=20, weight=ft.FontWeight.BOLD)
    c1 = ft.Checkbox(label="Preto", value=False)
    c2 = ft.Checkbox(label="Cinza", value=False)
    c3 = ft.Checkbox(label="Bege", value=False)
    c4 = ft.Checkbox(label="Siamês", value=False)
    c5 = ft.Checkbox(label="Branco", value=False)
    c6 = ft.Checkbox(label="Marrom", value=False)
    c7 = ft.Checkbox(label="Amarelo", value=False)
    c8 = ft.Checkbox(label="Laranja", value=False)
    c9 = ft.Checkbox(label="Tigrada", value=False)
    c10 = ft.Checkbox(label="Tigrada Preto ou Cinza", value=False)
    c11 = ft.Checkbox(label="Tigrada Amarelo ou Branco", value=False)
    c12 = ft.Checkbox(label="Sem Pelagem", value=False)
    c13 = ft.Checkbox(label="Escama", value=False)
    c14 = ft.Checkbox(label="Outros", value=False)
    b = ft.ElevatedButton(text="Salvar", on_click=button_clicked)

    page_.add(
        ft.Row([t],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Container(height=2),
        ft.Row([
            ft.Column([c1, c2, c3, c4, c5, c6, c7]),
            ft.Container(width=50),
            ft.Column([c8, c9, c10, c11, c12, c13, c14])
        ]),
        ft.Row([
            ft.Column(
                [ft.Container(
                    content=b,
                    padding=10
                )],
            )
        ],
        alignment=ft.MainAxisAlignment.END
        )
    )


def main(page: ft.Page, estado = None):
    page.title = "Cadastrar Animal"
    data_field = ft.TextField(
        hint_text='Data',
        read_only=True,
        focused_border_color=ft.colors.BLACK,
        value='',
        width=180,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.BLACK,
        border_radius=10
        )
    def change_date(e):
        data_field.value = date_picker.value.date()
        page.update()

    date_picker = ft.DatePicker(
        on_change=change_date
    )

    data_castracao = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_color=ft.colors.BLACK,
        height=50,
        width=50,
        on_click=lambda _: date_picker.pick_date()  
        )
    
    page.overlay.append(date_picker)


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

    img_animal_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'animal.png')


    avatar = ft.CircleAvatar(
        foreground_image_src=img_animal_path,
        content=ft.Text("LOAD"),
        )

    img_perfil = ft.Container(
        avatar,
        width=120,
        height=120,
    )


    def perfil_picked(e: ft.FilePickerResultEvent):
        if e.files:
            avatar.foreground_image_src = e.files[0].path
            page.update()


    file_picker = ft.FilePicker(
        on_result=perfil_picked
    )


    page.overlay.append(file_picker)


    upload_img = ft.Container(
        col=8,
        content=ft.Row(
            controls=[
                ft.ElevatedButton("Escolher Foto",
                                  on_click=lambda _: file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE),
                                  bgcolor="#D9D9D9",
                                  icon=ft.icons.FOLDER_OPEN_OUTLINED,
                                  color=ft.colors.BLACK)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=126
    )


    animal_castrado = ft.Dropdown(
        width=172,
        options=[
            ft.dropdown.Option("Castrado"),
            ft.dropdown.Option("Não castrado"),
        ],
        hint_text="É castrado?",
        alignment=ft.alignment.center,
        border_radius=8
    )


    obs_cast = ft.TextField(
                value="",
                hint_text="Observações castração",
                width=172, multiline=True,
                min_lines=7, max_lines=7,
            )

    campo_obs_cad = ft.Container(
        content=obs_cast,
    )


    nome_protegido = ft.TextField(
        col=4,
        label="Nome do protegido", 
        value="",
        width=172,
        # height=56,
        border_radius=8,
    )


    genero = ft.Dropdown(
        col=4,
        hint_text="Gênero",
        width=172,
        options=[
            ft.dropdown.Option("Masc."),
            ft.dropdown.Option("Fem."),
            ft.dropdown.Option("Desc.")
        ],
        border_radius=8
    )


    temperamento = ft.Dropdown(
        col=4,
        width=172,
        hint_text="Temperamento",
        options=[
            ft.dropdown.Option("Calmo"),
            ft.dropdown.Option("Raivoso"),
            ft.dropdown.Option("Sociável"),
            ft.dropdown.Option("Dócil e não convive com outros"),
            ft.dropdown.Option("Dócil e convive com outros"),
            ft.dropdown.Option("Sem Reação"),
            ft.dropdown.Option("Outro"),
        ],
        alignment=ft.alignment.center,
        border_radius=8
    )

    especie = ft.TextField(
        col=4,
        label="Especie",
        value="",
        width=172,
        # height=56,
        border_radius=8,
    )


    button_style = ft.ButtonStyle(
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        shape=ft.RoundedRectangleBorder(radius=8),
        side=ft.BorderSide(width=2, color=ft.colors.BLACK),
        padding=10 
    )


    def popup_pelagem(e):
        def run_popup():
            ft.app(target=popup)
        p2 = multiprocessing.Process(target=run_popup)
        p2.start()
        p2.join()


    pelagem = ft.OutlinedButton(
        text="Selecionar Pelagem",
        col=4,
        width=172,
        height=56,
        on_click=popup_pelagem,
        style=button_style
    )


    raca =  ft.TextField(
        col=4,
        label="Raça",
        value="",
        width=172,
        # height=56,
        border_radius=8,
    )


    porte = ft.Dropdown(
        col=4,
        width=172,
        hint_text="Porte",
        options=[
            ft.dropdown.Option("Pequeno"),
            ft.dropdown.Option("Médio"),
            ft.dropdown.Option("Grande")
        ],
        border_radius=8
    )


    status_atual = ft.Dropdown(
        col=4,
        width=172,
        hint_text="Status Atual",
        options=[
            ft.dropdown.Option("Abrigado"),
            ft.dropdown.Option("Adotado"),
            ft.dropdown.Option("Óbito")  # Quando o status é mudado para óbito um campo data de óbito e observações de óbito devem aparecer para serem preenchidos
        ],
        border_radius=8
    )


    mocrochip = ft.Dropdown(
        col=4,
        width=172,
        hint_text="Microchip",
        options=[
            ft.dropdown.Option("Sim"),
            ft.dropdown.Option("Não"),
        ],
        border_radius=8
    )


    possui_seq = ft.Dropdown(
        col=4,
        width=172,
        hint_text="Possui sequela",
        options=[
            ft.dropdown.Option("Sim"),
            ft.dropdown.Option("Não"),
        ],
        border_radius=8,
    )


    idade = ft.TextField(
        col=3,
        label="Idade",
        value="",
        width=60,
        # height=56,
        border_radius=8,
    )


    idade_tipo = ft.Dropdown(
        col=3,
        width=172,
        hint_text="Tipo",
        options=[
            ft.dropdown.Option("Anos"),
            ft.dropdown.Option("Meses"),
        ],
        border_radius=8
    )


    def save_func(e):
        foto_animal = open(avatar.foreground_image_src, "rb").read()
        nome_animal = nome_protegido.value
        genero_animal = genero.value
        temperamento_animal = temperamento.value
        especie_animal = especie.value
        pelagem_aniamal = ', '.join(q.get())
        raca_animal = raca.value
        porte_animal = porte.value
        status_animal = status_atual.value
        tem_microchip = mocrochip.value
        animal_possui_sequela = possui_seq.value
        idade_animal = int(idade.value)
        idade_tipo_animal = idade_tipo.value
        e_castrado = animal_castrado.value
        data_castracao_animal = data_field.value
        obs_animal = obs.value
        obs_cast_animal = obs_cast.value

        animal_registado = animal.InfoAnimal(
            nome_animal=nome_animal,
            especie=especie_animal,
            foto=foto_animal,
            genero=genero_animal,
            temperamento=temperamento_animal,
            idade=idade_animal,
            medida_idade=idade_tipo_animal,
            porte=porte_animal,
            pelagem=pelagem_aniamal,
            raca=raca_animal,
            microchip=tem_microchip,
            status_atual=status_animal,
            possui_sequela=animal_possui_sequela,
            observacoes=obs_animal
        )


        def verificar_variaveis_vazias(**kwargs):
            variaveis_vazias = [nome for nome, valor in kwargs.items() if not valor]
            return variaveis_vazias if variaveis_vazias else None


        # Verificação
        variaveis_vazias = verificar_variaveis_vazias(
            foto_animal=foto_animal,
            nome_animal=nome_animal,
            genero_animal=genero_animal,
            temperamento_animal=temperamento_animal,
            especie_animal=especie_animal,
            pelagem_aniamal=pelagem_aniamal,
            raca_animal=raca_animal,
            porte_animal=porte_animal,
            status_animal=status_animal,
            tem_microchip=tem_microchip,
            animal_possui_sequela=animal_possui_sequela,
            idade_animal=idade_animal,
            idade_tipo_animal=idade_tipo_animal,
            e_castrado=e_castrado,
            data_castracao_animal=data_castracao_animal,
            obs_animal=obs_animal,
            obs_cast_animal=obs_cast_animal
        )


        if not variaveis_vazias:
            print("to db")
            id_animal = db.add_animal(animal_registado)
            print(id_animal)

            castracao_animal_registrado = animal.Castracao(
                id_animal=id_animal,
                data_castracao=data_castracao_animal,
                castrado=e_castrado,
                observacoes=obs_cast_animal
            )

            db.add_castracao(castracao_animal_registrado)

            page.clean()
            estado.estado = "Tela de Cadastro de Resgate"
            estado.main_page()
        else:
            if not nome_animal:
                nome_protegido.error_text = "Preencha Nome do Animal"
            if not genero_animal:
                genero.error_text = "Escolha o Gênero do Animal"
            if not temperamento_animal:
                temperamento.error_text = "Escolha o Temperamento do Animal"
            if not especie_animal:
                especie.error_text = "Escolha a Especie do Animal"
            if not raca_animal:
                raca.error_text = "Preencha a Raça do Animal"
            if not porte_animal:
                porte.error_text = "Preencha o Porte do Animal"
            if not status_animal:
                status_atual.error_text = "Escolha Status do Animal"
            if not tem_microchip:
                mocrochip.error_text = "Campos Obrigatório"
            if not animal_possui_sequela:
                possui_seq.error_text = "Campos Obrigatório"
            if not idade_animal:
                idade.error_text = "Preencha a Idade do Animal"
            if not idade_tipo_animal:
                idade_tipo.error_text = "Campos Obrigatório"
            if not e_castrado:
                animal_castrado.error_text = "Campos Obrigatório"
            if not data_castracao_animal:
                data_field.error_text = "Preencha Data de Castração"
            if not obs_animal:
                obs.error_text = "Campos Obrigatório"
            if not obs_cast_animal:
                obs_cast.error_text = "Campos Obrigatório"
            page.update()


    submit_button = ft.ElevatedButton(
        text="Salvar",
        on_click=save_func,
        color=ft.colors.BLACK
    )

    basic_info = ft.ResponsiveRow(
        col=3,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        controls=[
            icon_return,
            img_perfil,
            upload_img,
            animal_castrado,
            ft.Row([
                data_field,
                data_castracao
            ]),
            campo_obs_cad
        ]
    )


    info_insert = ft.Container(
        padding=80,
        col=12,
        content=ft.ResponsiveRow(
            controls=[
                nome_protegido,
                genero,
                temperamento,
                especie,
                pelagem,
                raca,
                porte,
                status_atual,
                mocrochip,
                possui_seq,
                idade, idade_tipo
            ]
        )
    )

    obs = ft.TextField(
            hint_text="Observações",
            value="",
            multiline=True,
            min_lines=5,
            max_lines=5,
        )

    info_obs = ft.Container(
        col=12,
        content=obs,
        width=300,
    )
    
    infos_add = ft.ResponsiveRow(
        col=8,
        controls=[
           info_insert,
           info_obs
        ],
        expand=True
    )
    
    layout = ft.ResponsiveRow(
        spacing=70,
        col=12,
        controls=[
            basic_info,
            infos_add,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(layout)
    page.overlay.append(file_picker)

    page.add(
        ft.Container(
            content=submit_button,
            alignment=ft.alignment.bottom_right,
            padding=ft.padding.only(right=20, bottom=20)
        )
    )


def run_main():
    ft.app(target=main)


def run_popup():
    ft.app(target=popup)


if __name__ == "__main__":
    multiprocessing.freeze_support()

    # Crie e inicie os processos
    p1 = multiprocessing.Process(target=run_main)

    p1.start()

    # Opcional: Esperar que os processos terminem antes de sair
    p1.join()
