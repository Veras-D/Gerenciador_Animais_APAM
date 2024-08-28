import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import Models.Repository.db as database
import Models.Entities.animal as animal


def main(page):
    page.title = "Adicionar Resgate ao Animal"
    page.theme_mode = ft.ThemeMode.LIGHT
    atendimento = ft.TextField(
        label="Atendimento",
        value="",
        width=650,
        height=56,
        border_radius=8,
    )
    obs_resgate = ft.TextField(
        hint_text="Observações de Resgate",
        value="",
        width=320,
        border_radius=8,
        multiline=True,
        min_lines=7,
        max_lines=7,
    )
    hist_anam = ft.TextField(
        hint_text="Histórico de ANAMNESE",
        value="",
        width=320,
        border_radius=8,
        multiline=True,
        min_lines=7,
        max_lines=7,
    )
    dest_prot = ft.TextField(
        label="Destinação do Protegido",
        value="",
        width=370,
        height=56,
        border_radius=8,
    )
    inter_e_medi = ft.TextField(
        label="Tratamento, Intervenção e Medicação",
        value="",
        width=320,
        height=56,
        border_radius=8,
    )
    local_resga = ft.TextField(
        label="Local Resgate",
        value="",
        width=430,
        height=56,
        border_radius=8,
    )
    diagnostico = ft.TextField(
        label="Diagnostico - Estado de Saúde",
        value="",
        width=320,
        height=56,
        border_radius=8,
    )
    data_resga = ft.TextField(
        hint_text='Data de Resgate',
        read_only=True,
        focused_border_color=ft.colors.BLACK,
        value='',
        width=210,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    def change_date(e):
        data_resga.value = date_picker.value.date()
        page.update()

    date_picker = ft.DatePicker(
        on_change=change_date
    )
    bnt_data_resga = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_color=ft.colors.BLACK,
        height=50,
        width=50,
        on_click=lambda _: date_picker.pick_date()
    )
    page.overlay.append(date_picker)
    inter_curu = ft.Dropdown(
        width=210,
        options=[
            ft.dropdown.Option("Sim"),
            ft.dropdown.Option("Não"),
        ],
        hint_text="Intervenção Cirúrgica",
        alignment=ft.alignment.center,
        border_radius=8
    )


    def save_func(e):
        valor_atendimento = atendimento.value
        valor_local_resgate = local_resga.value
        valor_dest_prot = dest_prot.value
        valor_diagnostico = diagnostico.value
        valor_intervencao_cirurgica = inter_curu.value
        valor_data_resgate = data_resga.value
        valor_interven_e_medicacao = inter_e_medi.value
        valor_hist_anam = hist_anam.value
        valor_obeservacao_resgate = obs_resgate.value

        if not valor_data_resgate:
            data_resga.error_text = "Campo Obrigatório"
        else:
            info_resgate = animal.InfoResgate(
                id_animal=pass,
                local_resgate=valor_local_resgate,
                atendimento=valor_atendimento,
                necessario_intervencao_cirurgica=valor_intervencao_cirurgica,
                destinacao_do_protegido=valor_dest_prot,
                historico_anamnese=valor_hist_anam,
                diagnostico_estado_saude=valor_diagnostico,
                tratamento_intervencao_e_medicacao=valor_interven_e_medicacao,
                data_resgate=valor_data_resgate,
                observacoes=valor_obeservacao_resgate
            )

            database.add_resgate(info_resgate)


    bnt_salvar = ft.ElevatedButton(
        text="Salvar",
        on_click=save_func,
        color=ft.colors.BLACK
    )


    page.add(
        ft.Row([
            ft.Container(height=40)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            atendimento,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            local_resga,
            inter_curu,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            dest_prot,
            data_resga, bnt_data_resga,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            diagnostico,
            inter_e_medi,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Container(height=5),
        ft.Row([
            obs_resgate,
            hist_anam,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Container(height=20),
        ft.Row([
            ft.Container(width=900),
            bnt_salvar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        width=650
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)
