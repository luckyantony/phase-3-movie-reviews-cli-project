from db.connections import CURSOR, CONN

class Review:
    def __init__(self, reviewer_id, movie_id, rating, comment, id=None):
        self.id = id
        self.reviewer_id = reviewer_id
        self.movie_id = movie_id
        self.rating = rating
        self.comment = comment

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO reviews (reviewer_id, movie_id, rating, comment) VALUES (?, ?, ?, ?)",
                           (self.reviewer_id, self.movie_id, self.rating, self.comment))
            CONN.commit()
            self.id = CURSOR.lastrowid

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM reviews")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    def __str__(self):
        return f"Review(id={self.id}, reviewer_id={self.reviewer_id}, movie_id={self.movie_id}, rating={self.rating}, comment='{self.comment}')"