import sqlite3

CONN = sqlite3.connect('movie_reviews.db')
CURSOR = CONN.cursor()

