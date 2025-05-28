from db.connection import CURSOR, CONN

class Movie:
    def __init__(self, title, genre, id=None):
        self.id = id
        self.title = title
        self.genre = genre

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", (self.title, self.genre))
            CONN.commit()
            self.id = CURSOR.lastrowid

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM movies")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]

    def __str__(self):
        return f"Movie(id={self.id}, title='{self.title}', genre='{self.genre}')"