from io import open

people = []

with open("people.txt", "r", encoding="utf8") as people_file:
    for person in people_file:
        person = person.split(";")
        
        person = {
            "id": person[0],
            "name": person[1],
            "surname": person[2],
            "birthday": person[3].replace("\n", "")
        }
        
        people.append(person)

for person in people:
    print(
        f"Name: {person['name']}, Surname: {person['surname']}, Birthday: {person['birthday']}"
    )
