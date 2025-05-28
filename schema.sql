DROP TABLE IF EXISTS reviewers;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS reviews;

CREATE TABLE reviewers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reviewer_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    comment TEXT,
    FOREIGN KEY (reviewer_id) REFERENCES reviewers(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);
