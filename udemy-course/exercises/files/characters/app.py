from models import Character, Manager

warrior = Character("Warrior", 150, 34, 35, 15)
knight = Character("Knight", 200, 27, 43, 10)
archer = Character("Archer", 70, 41, 16, 50)

testing = Character("test", 4, 5, 6, 7)

manager = Manager()

manager.add_character(warrior)
manager.add_character(knight)
manager.add_character(archer)

manager.add_character(testing)
manager.delete_character("test")

manager.show_characters()
