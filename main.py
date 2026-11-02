import webview
import sys
import os

def get_resource_path(relative_path):
    """Функция для корректного получения пути к ресурсам"""
    try:
        # PyInstaller создает временную директорию
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    # Получаем путь к HTML-файлу
    html_path = get_resource_path('index.html')
    
    # Создаем окно с игрой
    webview.create_window(
        'Авантюристы: Забег',
        html_path,
        width=800,
        height=500,
        resizable=False
    )
    webview.start()
