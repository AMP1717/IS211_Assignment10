import sqlite3

DB_FILE = "pets.db"

def create_database():
    open(DB_FILE, "w")
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    person = \
"""CREATE TABLE person(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);"""

    pet = \
"""CREATE TABLE pet(
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);"""

    person_pet = \
"""CREATE TABLE person_pet(
    person_id INTEGER,
    pet_id INTEGER
);"""

    cur.execute(person)
    cur.execute(pet)
    cur.execute(person_pet)
    cur.close()
    conn.commit()
    conn.close()

def fill_database():
    person = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]

    pet = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]

    person_pet = [
        (1,1),
        (1,2),
        (2,3),
        (2,4),
        (3,5),
        (4,6)
    ]

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)
    cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)
    cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)
    cur.close()
    conn.commit()
    conn.close()

""" 
Answer to question 2

Person_pet table describes relation between a person and a pet.

Since right now each pat only has 1 owner, person_pet table could be replaced by 
adding new attribute to pet table, whis attribute would reference the owner of the 
pet using the person_id as foreign key.

Thats said, this table allows us to have 2 (or more) owners for one pet.

"""

create_database()       # create database file, create tables
fill_database()         # fill tables with data
