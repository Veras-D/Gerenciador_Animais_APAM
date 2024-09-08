import flet as ft

class Data:
    def __init__(self) -> None:
        self.counter = 0

d = Data()

def main(page):

    page.snack_bar = ft.SnackBar(
        content=ft.Text("Hello, world!", color=ft.colors.WHITE),
        # action="Alright!",
        bgcolor=ft.colors.RED,
        # action_color=ft.colors.RED,
    )

    def on_click(e):
        # page.snack_bar = ft.SnackBar(ft.Text(f"Hello {d.counter}"))
        page.snack_bar.open = True
        d.counter += 1
        page.update()

    page.add(ft.ElevatedButton("Open SnackBar", on_click=on_click))

ft.app(main)
