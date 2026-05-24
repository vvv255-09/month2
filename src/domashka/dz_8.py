import sqlite3

conn = sqlite3.connect("cinema.db")
cur = conn.cursor()

cur.executescript("""
    DROP TABLE IF EXISTS reviews;
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS movies;

    CREATE TABLE users (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );

    CREATE TABLE movies (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL
    );

    CREATE TABLE reviews (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id  INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        rating   INTEGER CHECK(rating BETWEEN 1 AND 10),
        FOREIGN KEY(user_id)  REFERENCES users(id),
        FOREIGN KEY(movie_id) REFERENCES movies(id)
    );
""")

# 5 пользователей
cur.executemany(
    "INSERT INTO users (name) VALUES (?)",
    [("Алина",), ("Борис",), ("Вика",), ("Гарик",), ("Дана",)]
)

# 5 фильмов
cur.executemany(
    "INSERT INTO movies (title, genre) VALUES (?, ?)",
    [
        ("Начало",             "Фантастика"),
        ("Интерстеллар",       "Фантастика"),
        ("Зеленая миля",       "Драма"),
        ("Темный рыцарь",      "Боевик"),
        ("Волк с Уолл-стрит",  "Драма"),
    ]
)

# 10 отзывов
cur.executemany(
    "INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)",
    [
        (1, 1, 9),  (1, 2, 10),
        (2, 1, 7),  (2, 3, 8),
        (3, 3, 10), (3, 4, 9),
        (4, 2, 6),  (4, 4, 8),
        (5, 1, 5),  (5, 5, 7),
    ]
)

conn.commit()
print("✅ Таблицы созданы и заполнены")

def print_table(title: str, cursor: sqlite3.Cursor) -> None:
    rows = cursor.fetchall()
    cols = [d[0] for d in cursor.description]
    col_widths = [max(len(str(c)), *(len(str(r[i])) for r in rows))
                  for i, c in enumerate(cols)]
    sep = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    header = "|" + "|".join(f" {c:<{col_widths[i]}} " for i, c in enumerate(cols)) + "|"

    print(f"\n{'─' * 50}")
    print(f"  {title}")
    print(f"{'─' * 50}")
    print(sep)
    print(header)
    print(sep)
    for row in rows:
        print("|" + "|".join(f" {str(v):<{col_widths[i]}} " for i, v in enumerate(row)) + "|")
    print(sep)
    print(f"  Строк: {len(rows)}")

cur.execute("""
    SELECT
        u.name   AS пользователь,
        m.title  AS фильм,
        r.rating AS оценка
    FROM reviews r
    JOIN users  u ON u.id = r.user_id
    JOIN movies m ON m.id = r.movie_id
    ORDER BY u.name, r.rating DESC
""")
print_table("JOIN: пользователь + фильм + оценка", cur)

cur.execute("""
    SELECT
        m.title              AS фильм,
        COUNT(r.id)          AS кол_отзывов,
        ROUND(AVG(r.rating), 1) AS средняя_оценка
    FROM movies m
    LEFT JOIN reviews r ON m.id = r.movie_id
    GROUP BY m.id, m.title
    ORDER BY средняя_оценка DESC
""")
print_table("LEFT JOIN: все фильмы (даже без отзывов)", cur)

cur.execute("""
    SELECT
        m.title                  AS фильм,
        ROUND(AVG(r.rating), 1)  AS средняя,
        MAX(r.rating)            AS максимум,
        MIN(r.rating)            AS минимум
    FROM movies m
    JOIN reviews r ON m.id = r.movie_id
    GROUP BY m.id, m.title
    ORDER BY средняя DESC
""")
print_table("АГРЕГАЦИИ: статистика по каждому фильму", cur)

cur.execute("""
    SELECT
        ROUND(AVG(rating), 2) AS средняя_по_всем,
        MAX(rating)           AS макс_оценка,
        MIN(rating)           AS мин_оценка
    FROM reviews
""")
print_table("АГРЕГАЦИИ: общая статистика по всем отзывам", cur)

conn.close()
print("\n✅ Готово! База сохранена в файл cinema.db")