import psycopg2
from psycopg2 import sql

# Параметри підключення до БД
connection_params = {
    "user": "postgres",
    "password": "123456",
    "host": "localhost",
    "port": "5432"
}

# Ім'я бази даних, яку потрібно створити
db_name = "tasks_01"

if __name__ == "__main__":
    try:
        # Підключаємося до PostgreSQL без зазначення БД
        conn = psycopg2.connect(**connection_params)
        conn.autocommit = True  # Встановлення автокоміту для виконання операцій без транзакцій

        
        cur = conn.cursor()

        # Створюємо базу даних 
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

        
        cur.close()
        conn.close()

        print("База даних успішно створена!")

        # Підключаємося до створеної БД
        conn = psycopg2.connect(database=db_name, **connection_params)
        conn.autocommit = True
        cur = conn.cursor()

        # Виконуємо вміст файлу tasks.sql
        with open('tasks.sql', 'r') as f:
            sql_script = f.read()
            cur.execute(sql_script)

    
        cur.close()
        conn.close()

    except psycopg2.errors.DuplicateDatabase:
        print("База даних вже існує.")
    except Exception as e:
        print("Помилка!:", e)
