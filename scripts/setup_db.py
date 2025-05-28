import sqlite3

with open("schema.sql") as f:
    schema = f.read()

conn = sqlite3.connect("movie_reviews.db")
cursor = conn.cursor()
cursor.executescript(schema)
conn.commit()
conn.close()
print("Database schema created.")
