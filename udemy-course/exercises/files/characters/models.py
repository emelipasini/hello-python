from io import open
import pickle

class Character:
    def __init__(self, name, health, attack, defense, range):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.range = range
    
    def __str__(self):
        return f"{self.name.upper()}: {self.health} health, {self.attack} attack " \
            f"{self.defense} defense, {self.range} range"

class Manager:
    characters = []

    def __init__(self):
        self.read_file()

    def read_file(self):
        try:
            file = open("characters.pckl", "ab+")
            file.seek(0)
            self.characters = pickle.load(file)
            file.close()
        except:
            print("Empty file")
    
    def show_characters(self):
        if len(self.characters) > 0:
            for character in self.characters:
                print(character)
        else:
            print("No characters saved")
    
    def find_character(self, name):
        for element in self.characters:
            if element.name.upper() == name.upper():
                return element
    
    def add_character(self, character):
        exists = self.find_character(character.name)
        if not exists:
            self.characters.append(character)
            self.save_file()
        else:
            print("Already saved")

    def delete_character(self, name):
        character = self.find_character(name)
        if character:
            self.characters.remove(character)
            self.save_file()
        else:
            print("Character not found")
        
    def save_file(self):
        file = open("characters.pckl", "wb")
        pickle.dump(self.characters, file)
        file.close()
