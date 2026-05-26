#!/usr/bin/env python3
"""
Генератор .m3u8 плейлиста для канала FilmsTop.
Создает файл stream.m3u8 с логотипом и списком фильмов из базы данных.
Логотип отображается как текстовая надпись "LiveM3U Films" в углу (через комментарий или заглушку).
Примечание: Реальное наложение логотипа (watermark) требует перекодирования видео через FFmpeg.
Этот скрипт генерирует стандартный HLS плейлист.
"""

import film_manager
import os

CHANNEL_NAME = "LiveM3U Films"
LOGO_TEXT = "LiveM3U Films"
OUTPUT_FILE = "stream.m3u8"

def generate_m3u8():
    films = film_manager.get_all_films()
    
    if not films:
        print("База данных пуста. Невозможно сгенерировать плейлист.")
        # Создаем пустой плейлист с информацией о канале
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write("#EXTM3U\n")
            f.write(f"#EXTINF:-1 tvg-logo=\"logo.png\" group-title=\"Movies\",{CHANNEL_NAME}\n")
            f.write("# Плейлист пуст. Добавьте фильмы в базу данных.\n")
        print(f"Создан пустой плейлист {OUTPUT_FILE}")
        return

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        # Заголовок канала с логотипом (логотип должен быть файлом logo.png в той же папке или URL)
        # В реальном стриминге логотип накладывается сервером или плеером
        f.write(f"#EXTINF:-1 tvg-name=\"{CHANNEL_NAME}\" tvg-logo=\"https://via.placeholder.com/200x100.png?text=LiveM3U+Films\" group-title=\"Movies\",{CHANNEL_NAME} - 24/7\n")
        
        # Для демонстрации 24/7 вещания мы просто перечисляем файлы.
        # Настоящее бесшовное вещание требует использования FFmpeg для склейки файлов в поток.
        for film in films:
            fid, title, desc, path = film
            # Добавляем каждый фильм как элемент плейлиста
            f.write(f"#EXTINF:-1,{title}\n")
            f.write(f"{path}\n")
            
    print(f"Плейлист {OUTPUT_FILE} успешно сгенерирован с {len(films)} фильмами.")
    print(f"Название канала: {CHANNEL_NAME}")
    print(f"Для отображения логотипа убедитесь, что ваш плеер поддерживает тег tvg-logo.")

if __name__ == "__main__":
    generate_m3u8()
