import flet as ft
import time

last_click_time = 0

def main(page: ft.Page):
    global last_click_time
    page.padding = 0
    page.bgcolor = "#A9CCF2"
    page.window_full_screen = True
    page.window_maximized = True
    page.window_resizable = False

    # Обработчик кликов для закрытия окна
    def handle_click(e):
        global last_click_time
        current_time = time.time()
        if current_time - last_click_time < 0.3:
            page.window_close()
        else:
            last_click_time = current_time

    # Векторный фон слева
    splash_container_image = ft.Image(
        src="assets/images/Vector 2.png",  # Путь к изображению
        height=page.window_height,          
        fit=ft.ImageFit.COVER
    )

    # Контейнер для фонового изображения слева
    left_side = ft.Container(
        content=splash_container_image,
        width=page.window_width // 2,  # 50% ширины страницы
        height=page.window_height,
        alignment=ft.alignment.top_left,
        expand=False
    )

    # Логотип
    logo = ft.Image(
        src="assets/images/logo.png",  
        width=150,
        height=150,
    )

    # Стиль текста
    text_style = ft.TextStyle(
        size=55,
        color="#005C9F",
        weight="bold",
        font_family="Titletxt"
    )

    # Контент с текстом и логотипом в правом нижнем углу
    splash_content = ft.Column(
        [
            logo,
            ft.Text("My HealthTrack", style=text_style)
        ],
        alignment="end",  # Выравнивание по вертикали внизу
        horizontal_alignment="end",  # Выравнивание по горизонтали справа
    )

    # Контейнер для правой части с текстом и изображением
    right_side = ft.Container(
        content=splash_content,
        width=page.window_width // 2,  # 50% ширины страницы
        height=page.window_height,
        alignment=ft.alignment.bottom_right,  # Выравнивание по правому нижнему углу
        expand=False
    )

    # Добавление элементов на страницу
    page.add(left_side, right_side)

    # Таймер с задержкой 3 секунды (если необходимо)
    time.sleep(3)

    # Очищаем страницу
    page.clean()

    # Подключение шрифта через CSS
    page.stylesheet = """
    @font-face {
        font-family: 'Titletxt';
        src: url('assets/fonts/js-regular.ttf');  # Убедитесь, что путь правильный
    }
    """

ft.app(target=main)