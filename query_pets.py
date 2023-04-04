import sqlite3

DB_FILE = "pets.db"

def get_number():
    while True:
        n = input("Enter person id: ")
        try:
            n = int(n)
            return n
        except ValueError:
            continue

def print_person(uid, cur):
    person = cur.execute(f"SELECT * FROM person WHERE person.id = {uid};").fetchone()
    if person:
        print(f"{person[1]} {person[2]}, {person[3]} years old.")
        return True
    else:
        print("No such user.")
        return False


def print_pets(uid, cur):
    sql = \
    f"""
    SELECT * FROM person
    JOIN person_pet ON person.id = person_pet.person_id
    JOIN pet ON person_pet.pet_id = pet.id
    WHERE person.id = {uid}
    """

    for result in cur.execute(sql):
        _, fname, sname, _, _, _, _, pname, pbreed, page, pdead = result
        if pdead == 0:
            print(f"{fname} {sname} owns {pname}, a {pbreed}, currently {page} years old.")
        else:
            print(f"{fname} {sname} owned {pname}, a {pbreed}, that was {page} years old.")


def main():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    while True:
        person_id = get_number()
        if person_id == -1:
            break
        if not print_person(person_id, cur):
            continue
        print_pets(person_id, cur)

    cur.close()
    conn.close()

main()
