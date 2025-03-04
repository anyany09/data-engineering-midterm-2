import sqlite3

# ბაზის შექმნა
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# ცხრილის შექმნა
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# საწყისი მონაცემების დამატება
cursor.executemany("""
INSERT INTO users (name, age) VALUES (?, ?)
""", [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35)
])

# ცვლილებების შენახვა და კავშირის დახურვა
conn.commit()
conn.close()

print("Database initialized successfully!")
