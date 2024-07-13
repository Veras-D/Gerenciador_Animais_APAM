import flet as ft
import datetime

def main(page: ft.Page):

    class Example(ft.Column): #botao calendario
        def __init__(self):
            super().__init__()
            self.datepicker = ft.DatePicker(
                first_date=datetime.datetime(2023, 10, 1),
                last_date=datetime.datetime(2024, 10, 1),
                on_change=self.change_date,
            )
            self.selected_date = ft.Text()
            self.date_button = ft.ElevatedButton(
                width=172,
                content=ft.Row(
                    controls=[
                        ft.Text("Data castração"),
                        ft.Icon(ft.icons.CALENDAR_TODAY_OUTLINED, size=24)
                    ],
                    alignment="center"
                ),
                bgcolor=ft.colors.WHITE,
                color=ft.colors.BLACK,
                on_click=self.open_date_picker,
            )
            self.controls = [self.date_button, self.selected_date, self.datepicker]

        def open_date_picker(self, e):
            self.datepicker.pick_date()

        def change_date(self, e):
            self.selected_date.value = f"Data selecionada: {e.control.value.strftime('%Y-%m-%d')}"
            page.update()  
    example = Example()

    icon_return = ft.Container(
        content=ft.Icon(ft.icons.HOME_OUTLINED, size=24, color=ft.colors.BLACK),
        alignment=ft.alignment.center_left,
        url="#"
    )

    img_perfil = ft.Container(
        ft.Image(
            src="https://picsum.photos/600/600",
            width=120,
            height=120,
            border_radius=100,
        )
    )

    upload_img = ft.Container(
        col=8,
        content=ft.Row(
            controls=[
                ft.Text("Carregar foto"),
                ft.Icon(ft.icons.FOLDER_OPEN_OUTLINED, color=ft.colors.BLACK)
            ],
            alignment=ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo do Row
        ),
        width=126,
        bgcolor="#D9D9D9"
    )
  
    animal_castrado = ft.Dropdown(
        width=172,
        options=[
            ft.dropdown.Option("Castrado"),
            ft.dropdown.Option("Não castrado"),
        ],
        value="Castrado",
        alignment=ft.alignment.center,
        border_radius=8
    )

    campo_obs_cad = ft.Container(
            ft.TextField(
            value="",
            hint_text="Observações castração",
            width=172,height=143,
            
        ),
    )

    basic_info = ft.ResponsiveRow(
        col=3,
        expand=True,
        controls=[
            icon_return,
            img_perfil,
            upload_img,
            animal_castrado,
            example.date_button,  # calendario
            example.selected_date,  # calendario
            example.datepicker,  # calendario
            campo_obs_cad
        ]
    )

    nome_protegido = ft.TextField(
        col=4,
        label="Nome do protegido", 
        value="",
        width=172,
        height=56,
        border_radius=8,
    )

    genero = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Gênero"),
            ft.dropdown.Option("Masc."),
            ft.dropdown.Option("Fem."),
            ft.dropdown.Option("Desc.")
        ],
        value="Gênero",
        border_radius=8
    )

    temperamento = ft.Dropdown(
        col= 4,
        width=172,
        options=[
            ft.dropdown.Option("Temperamento"),
            ft.dropdown.Option("Calmo"),
            ft.dropdown.Option("Raivoso"),
            ft.dropdown.Option("Sociável"),
            ft.dropdown.Option("Dócil e não convive com outros"),
            ft.dropdown.Option("Dócil e convive com outros"),
            ft.dropdown.Option("Sem Reação"),
            ft.dropdown.Option("Outro"),

        ],
        value="Temperamento",
        alignment=ft.alignment.center,
        border_radius=8

    )

    especie = ft.TextField(
        col=4,
        label="Especie", 
        value="",
        width=172,
        height=56,
        border_radius=8,
    )

    pelagem = ft.Dropdown(
        col=4,  
        width=172,
        options=[
            ft.dropdown.Option("Pelagem"),
            ft.dropdown.Option("Preto"),
            ft.dropdown.Option("Cinza"),
            ft.dropdown.Option("Bege"),
            ft.dropdown.Option("Siamês"),
            ft.dropdown.Option("Branco"),
            ft.dropdown.Option("Marrom"),
            ft.dropdown.Option("Amarelo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Tigrada Marrom ou Preto"),
            ft.dropdown.Option("Tigrada Preto ou Cinza"),
            ft.dropdown.Option("Tigrada Amarelo ou Branco"),
            ft.dropdown.Option("Sem Pelagem"),
            ft.dropdown.Option("Escama"),
            ft.dropdown.Option("Outros"),
        ],  
        value="Pelagem",  
        border_radius=8, 
    )

    raca =  ft.TextField(
        col=4,
        label="Raça", 
        value="",
        width=172,
        height=56,
        border_radius=8,
    )
    
    porte = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Porte"),
            ft.dropdown.Option("Pequeno"),
            ft.dropdown.Option("Médio"),
            ft.dropdown.Option("Grande")
        ],
        value="Porte",
        border_radius=8
    )

    status_atual = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Status Atual"),
            ft.dropdown.Option("Abrigado"),
            ft.dropdown.Option("Adotado"),
            ft.dropdown.Option("Óbito") #Quando o status é mudado para óbito um campo data de óbito e observações de óbito devem aparecer para serem preenchidos
        ],
        value="Status Atual",
        border_radius=8
    )

    mocrochip = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Microchip"),
            ft.dropdown.Option("Sim"),
            ft.dropdown.Option("Não"),
        ],
        value="Microchip",
        border_radius=8
    )

    possui_seq = ft.Dropdown(
            col=4,
            width=172,
            options=[
                ft.dropdown.Option("Possui sequela"),
                ft.dropdown.Option("Sim"),
                ft.dropdown.Option("Não"),
            ],
            value="Possui sequela",
            border_radius=8,
            
        )
    
    idade = ft.TextField(
            col=3,
            label="Idade ", 
            value="",
            width=109,
            height=56,
            border_radius=8,
        )
    
    idade_tipo = ft.Dropdown(
        col=1,
        width=172,
        options=[
            ft.dropdown.Option("Tipo"),
            ft.dropdown.Option("Anos"),
            ft.dropdown.Option("Meses"),
        ],
        value="Tipo",
        border_radius=8
    )


    info_insert = ft.Container(
        padding=80,
        col=12,
        content= ft.ResponsiveRow(
            
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

    info_obs = ft.Container(
        col=12,
        content= ft.TextField(
            label="Observações", 
            value="",
            
        ),
        width=300,
        height=155
    ) 
                                

    infos_add = ft.ResponsiveRow(
        col=9,
        controls=[
           info_insert,
           info_obs
        ],
        expand=True
    )


    layout = ft.ResponsiveRow(
        col=12,
        controls=[
            basic_info,
            infos_add,
            
        ],
        expand=True
    )

    page.add( 
        layout,
    )

ft.app(target=main)
