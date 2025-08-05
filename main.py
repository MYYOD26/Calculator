import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.bgcolor = "#3560C5"
    page.window_width = 350
    page.window_height = 200
    page.padding = 10
    page.update()

    all_values =""

    result_text = ft.Text(value="0", size=28, color="white", text_align="right")

    def delete_last(e):
        nonlocal all_values
        all_values = all_values[:-1]  # ลบตัวสุดท้าย
        result_text.value = all_values if all_values else "0"
        page.update()
    def entering_values(e):
        nonlocal all_values
        all_values += str(e.control.text)
        result_text.value = all_values
        page.update()

    def clear_screen(e):
        nonlocal all_values
        all_values = ""
        result_text.value="0"
        page.update()

    def calculate(e):
        nonlocal all_values
        try:
            result_text.value = str(eval(all_values))
            all_values = result_text.value
        except:
            result_text.value ="Error"
            result_text.color ="red"
            all_values =""

        page.update()


    display = ft.Container(
        content=result_text,
        bgcolor="#1E2A78",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right,
    )

    number_style = {
        "height": 60,
        "bgcolor": "#1E2A78",
        "color": "white",
        "expand": 1,
    }
    operator_style = {
        "height": 60,
        "bgcolor": "#1E2A78",
        "color": "white",
        "expand": 1,
    }
    clear_style = {
        "height": 60,
        "bgcolor": "#C1843B",
        "color": "white",
        "expand": 1,
    }
    equal_style = {
        "height": 60,
        "bgcolor": "#553A9A",
        "color": "white",
        "expand": 1,
    }

    button_grid = [
        [
            ("C", clear_style, clear_screen),
            ("%", operator_style, entering_values),
            ("/", operator_style, entering_values),
            ("*", operator_style, entering_values),
        ],
        [
            ("7", number_style, entering_values),
            ("8", number_style, entering_values),
            ("9", number_style, entering_values),
            ("-", operator_style, entering_values),
        ],
        [
            ("4", number_style, entering_values),
            ("5", number_style, entering_values),
            ("6", number_style, entering_values),
            ("+", operator_style, entering_values),
        ],
        [
            ("1", number_style, entering_values),
            ("2", number_style, entering_values),
            ("3", number_style, entering_values),
            ("=", equal_style,calculate),
        ],
        [
            ("0", {**number_style, "expand": 2},entering_values),
            (".", number_style,entering_values),
            ("DEL", operator_style, delete_last),
        ],
    ]

    buttons = []
    for row in button_grid:
        row_controls = []
        for text, style, handler in row:
            btn = ft.ElevatedButton(
                text=text,
                on_click=handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0,
                )
            )
            row_controls.append(btn)
        buttons.append(ft.Row(row_controls, spacing=5))

    page.add(
        ft.Column([
            display,
            ft.Column(buttons, spacing=5)
        ],
        spacing=5)
    )

ft.app(target=main)
