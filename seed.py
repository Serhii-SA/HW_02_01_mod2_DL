import sqlite3
from faker import Faker
import random


fake = Faker()

# Функція для заповнення таблиці users
def seed_users(conn):
    cur = conn.cursor()

    for _ in range(12):  # Генеруємо 12 користувачів
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))
    conn.commit()

# Функція для заповнення таблиці status
def seed_status(conn):
    cur = conn.cursor()
    statuses = ['нове', 'в процесі', 'завершене']
    for status in statuses:
        cur.execute("INSERT INTO status (name) VALUES (?)", (status,))
    conn.commit()

# Функція для заповнення таблиці tasks
def seed_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cur.fetchall()]

    for _ in range(22):  # Генеруємо 22 завдання
        title = fake.sentence()
        description = fake.text()
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", (title, description, status_id, user_id))
    conn.commit()


def main():
    # Підключаємося до бази даних
    conn = sqlite3.connect('tasks.db')

    # Заповнюємо таблиці
    seed_users(conn)
    seed_status(conn)
    seed_tasks(conn)

   
    conn.close()

if __name__ == "__main__":
    main()
