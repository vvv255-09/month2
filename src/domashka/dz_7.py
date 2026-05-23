import sqlite3

from colorama import Fore, Style

conn = sqlite3.connect('store.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
    )
    """)
conn.commit()

def create_product(name, price, quantity):
    c.execute(''' INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)''',
              (name, price, quantity)
              )
    conn.commit()
    print(Fore.LIGHTGREEN_EX + 'Товар добавлен!!' + Style.RESET_ALL)

# create_product("Жвачка", 150.0, 100)
# create_product("Молоко", 89.5, 50)
# create_product("Хлеб", 45.0, 200)

def read_products():
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    if not products:
        print("Таблица пустая.")
    for row in products:
        print(Fore.LIGHTMAGENTA_EX + f"ID: {row[0]} | Название: {row[1]} | Цена: {row[2]} | Количество: {row[3]}" + Style.RESET_ALL)


read_products()

def update_product(id, price):
    c.execute("UPDATE products SET price = ? WHERE id = ?", (price, id))
    conn.commit()
    print(Fore.LIGHTBLUE_EX + f"Цена товара с ID {id} обновлена на {price}." + Style.RESET_ALL)

update_product(1, 100)

def delete_product(id):
    c.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    print(Fore.LIGHTRED_EX + f'Товрар с {id} был удвлен' + Style.RESET_ALL)

delete_product(1)
