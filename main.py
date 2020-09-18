import random
from os import name, system
from typing import List

class Data:
    def __init__(self, data, size):
        if data == None:
            self.data = self.generate_dataset(size)
        else:
            self.data = data

    def generate_dataset(self, size: int) -> List:
        data = []
        for x in range(size):
            x = x # Literally to stop git and vscode complaing that x is unused
            data.append(random.randint(0, 100))
        return data

    def bubble_sort(self) -> List:
        data = self.data
        sorted: bool = False
        while not sorted:
            swapped: bool = False
            for i in range(0, len(data)-1):
                if data[i] > data[i+1]:
                    swapped = True
                    data[i], data[i+1] = data[i+1], data[i]
            if swapped == False:
                sorted = True
        return data

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
        self.clear_screen()

        if choice == len(self.options)+1:
            quit()
        
        data = input("Type 'random' for random data or 'x,y,z' for own data.\n> ")
        if data == "random":
            data = None
            size = int(input("How many values?\n> "))
        else:
            data = eval(f"[{data}]")
            size = len(data)

        dataset = Data(data, size)

        if self.options[choice-1].split("_")[1] == "sort":
            print(f"Original Data: {dataset.data}")
            print(f"Sorted Data  : {eval(f'dataset.{self.options[choice-1]}()')}")

        else:
            print("search")

        input("...")
        self.show_menu()
        
    def clear_screen(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

if __name__ == "__main__":
    menu = Menu()