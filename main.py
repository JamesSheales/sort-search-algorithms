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
        self.options = ["bubble_sort", "insertion_sort"]
        self.show_menu()

    def show_menu(self):
        print(f"{15*'-'}Menu{15*'-'}")
        for option in self.options:
            print(option)
        print(34*"-")
    def clear_screen(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

if __name__ == "__main__":
    menu = Menu()