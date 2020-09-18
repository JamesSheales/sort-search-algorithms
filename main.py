import random
from os import name, system
from typing import List

class Data:
    def __init__(self, data=None):
        if data == None:
            self.data = self.generate_dataset(10)
        else:
            self.data = data

    def generate_dataset(self, size: int) -> List:
        data = []
        for x in range(size):
            x = x # Literally to stop git and vscode complaing that x is unused
            data.append(random.randint(0, 100))
        return data

    def bubble_sort(self, data: List) -> List:
        pass

    def insertion_sort(self, data: List) -> List:
        pass

    def merge_sort(self, data: List) -> List:
        pass

    def linear_search(self, data: List, val: int) -> List:
        pass

    def binary_search(self, data: List, val: int) -> List:
        pass

class Menu:
    def __init__(self):
        self.options = ["bubble_sort", "insertion_sort", "merge_sort", "linear_search"]
        self.show_menu()

    def get_nice_name(self, option: str) -> str:
        words = option.split("_")
        name = f"{words[0]} {words[1]}".title()
        return name

    def show_menu(self):
        self.clear_screen()
        print(f"{15*'-'}Menu{15*'-'}")
        for option in range(len(self.options)):
            print(f"{option+1}. {self.get_nice_name(self.options[option])}")
        print(f"{option+2}. Quit")
        print(34*"-")
        choice = int(input("> "))

        if choice == len(self.options)+1:
            self.clear_screen()
            quit()
        
        elif self.options[choice-1].split("_")[1] == "sort":
            print("sort")

        else:
            print("search")

        
    def clear_screen(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

if __name__ == "__main__":
    menu = Menu()