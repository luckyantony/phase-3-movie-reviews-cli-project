from db.connections import CURSOR, CONN

class Reviewer:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO reviewers (name) VALUES (?)", (self.name,))
            CONN.commit()
            self.id = CURSOR.lastrowid

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM reviewers")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[0]) for row in rows]

    @classmethod
    def delete_by_id(cls, id):
        CURSOR.execute("DELETE FROM reviewers WHERE id = ?", (id,))
        CONN.commit()

    def __str__(self):
        return f"Reviewer(id={self.id}, name='{self.name}')"
