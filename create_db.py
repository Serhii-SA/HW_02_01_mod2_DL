import sqlite3

if __name__ == "__main__":
    with open('tasks.sql', 'r') as f:
        sql = f.read()
        

# створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
# виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)



