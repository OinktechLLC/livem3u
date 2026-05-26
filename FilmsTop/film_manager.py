import sqlite3
from datetime import datetime

DB_NAME = 'films.db'

def add_film(title, description, file_path):
    """Добавляет фильм в базу данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO films (title, description, file_path)
        VALUES (?, ?, ?)
    ''', (title, description, file_path))
    
    conn.commit()
    conn.close()
    print(f"Фильм '{title}' добавлен в базу.")

def get_all_films():
    """Получает все фильмы из базы данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, title, description, file_path FROM films')
    films = cursor.fetchall()
    
    conn.close()
    return films

if __name__ == "__main__":
    # Пример добавления фильма (заглушка)
    add_film("Пример фильма", "Описание примера", "/path/to/movie.mp4")
