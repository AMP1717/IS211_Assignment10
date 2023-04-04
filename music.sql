CREATE TABLE artist(
    artist_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE album(
    album_id INTEGER PRIMARY KEY,
    name TEXT,
    artist_id INTEGER
);

CREATE TABLE song(
    song_id INTEGER PRIMARY KEY,
    name TEXT,
    track_number INTEGER,
    length INTEGER
    album_id INTEGER
);