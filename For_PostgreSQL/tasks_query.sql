-- Отримати всі завдання певного користувача (напр. - 5)
SELECT * FROM tasks WHERE user_id = 5;

-- Вибрати завдання за певним статусом (напр. 2 - in progress)
-- SELECT * FROM tasks WHERE status_id = 2; - Змінено на варіант з підзапитом по табл.status
SELECT * 
FROM tasks 
WHERE status_id = (SELECT id FROM status WHERE name = 'in progress');

-- Оновити статус конкретного завдання (id - 12).
-- Змініть статус конкретного завдання на 'in progress'
UPDATE tasks SET status_id = 2 WHERE id = 12;

-- Отримати список користувачів, які не мають жодного завдання.
SELECT id, fullname, email
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks);

-- Додати нове завдання для користувача - 5.
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Some task', 'Some descr.of task', 1, 5);

-- Отримати всі завдання, які ще не завершено.
SELECT * FROM tasks WHERE status_id <> 3;

-- Видалити завдання - 23
DELETE FROM tasks WHERE id = 23;

-- Знайти користувачів з певною електронною поштою.
SELECT * FROM users WHERE email LIKE '%@example.org';

-- Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
UPDATE users SET fullname = 'Bob' WHERE id = 1;

-- Отримати кількість завдань для кожного статусу.
-- Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
SELECT status_id, COUNT(*) AS task_count
FROM tasks
GROUP BY status_id;

-- Отримати завдання, які призначені користувачам з певною доменною частиною
-- електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN,
-- щоб вибрати завдання, призначені користувачам,
-- чия електронна пошта містить певний домен (наприклад, '%@example.com').
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';

-- Отримати список завдань, що не мають опису або опис NULL.
SELECT * FROM tasks WHERE description = '' OR description IS NULL;


-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
-- Використайте INNER JOIN для отримання списку користувачів та їхніх завдань
-- із певним статусом.
SELECT users.fullname, tasks.title
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
INNER JOIN status ON tasks.status_id = status.id
WHERE status.id = 2;

-- Отримати користувачів та кількість їхніх завдань.
-- Використайте LEFT JOIN та GROUP BY для вибору користувачів та
-- підрахунку їхніх завдань.(змінено на GROUP BY users.id )
SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id;