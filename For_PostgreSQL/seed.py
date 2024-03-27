# Подібно тому як було зроблено для SQLite заповнюємо табл.за допомогою Faker

import psycopg2
from faker import Faker
import random

fake = Faker()

def seed_users(conn):
    cur = conn.cursor()
    for _ in range(12):
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
    conn.commit()

def seed_status(conn):
    cur = conn.cursor()
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))
    conn.commit()

def seed_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cur.fetchall()]
    for _ in range(22):
        title = fake.sentence()
        description = fake.text()
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (title, description, status_id, user_id))
    conn.commit()

def main():
    conn = psycopg2.connect(
        dbname="tasks_01",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )

    seed_users(conn)
    seed_status(conn)
    seed_tasks(conn)

    conn.close()

if __name__ == "__main__":
    main()
