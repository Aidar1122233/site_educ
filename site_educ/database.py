import sqlite3
from contextlib import closing

def init_db():
    with closing(sqlite3.connect('courses.db')) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                title TEXT,
                category TEXT,
                price INTEGER
            )
        ''')
        cursor.executemany(
            'INSERT INTO courses (title, category, price) VALUES (?, ?, ?)',
            [
                ('Python для начинающих', 'Программирование', 5000),
                ('Маркетинг с нуля', 'Маркетинг', 3000)
            ]
        )
        conn.commit()

def get_courses():
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    return cursor.fetchall()

def get_cart(course_ids):
    if not course_ids:
        return []
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    placeholders = ','.join('?' for _ in course_ids)
    cursor.execute(f'SELECT * FROM courses WHERE id IN ({placeholders})', course_ids)
    return cursor.fetchall()


def add_to_cart():
    return None