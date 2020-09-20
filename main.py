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
            data.append(random.randint(0, 10000))
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

    def insertion_sort(self) -> List:
        data = self.data
        for i in range(1, len(data)):
            val = data[i]
            j=i-1
            while j>=0 and val < data[j]:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = val
        return data

    def merge_sort(self, data: List = None) -> List:
        if data == None:
            data = self.data
        if len(data) <= 1:
            return data
        mid = int(len(data) / 2)
        l, r = self.merge_sort(data[:mid]), self.merge_sort(data[mid:])
        return self.merge(l, r)

    def merge(self, l: List, r: List) -> List:
        sorted = []
        lIndex, rIndex = 0, 0

        while lIndex < len(l) and rIndex < len(r):
            if l[lIndex] < r[rIndex]:
                sorted.append(l[lIndex])
                lIndex += 1
            else:
                sorted.append(r[rIndex])
                rIndex += 1

        sorted.extend(l[lIndex:])
        sorted.extend(r[rIndex:])

        return sorted

    def linear_search(self, val: float) -> List:
        data = self.data
        positions = []
        for x in range(0, len(data)):
            if data[x] == val:
                positions.append(x)
        return positions

    def binary_search(self, val: int) -> List:
        data = self.merge_sort(self.data)
        lowerbound= 0
        upperbound= len(data)-1
        mid = 0

        while lowerbound <= upperbound:
            mid = (upperbound+lowerbound) // 2
            if data[mid] < val:
                lowerbound = mid + 1
            elif data[mid] > val:
                upperbound = mid - 1
            else:
                return mid

        return None

class Menu:
    def __init__(self):
        self.options = ["bubble_sort", "insertion_sort", "merge_sort", "linear_search", "binary_search"]
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
            self.clear_screen()
            print(10*"-"+self.get_nice_name(self.options[choice-1])+10*"-")
            print(f"Original Data: {dataset.data}")
            print(f"Sorted Data  : {eval(f'dataset.{self.options[choice-1]}()')}")

        else:
            val = float(input("What number are you trying to locate?\n> "))
            self.clear_screen()
            print(10*"-"+self.get_nice_name(self.options[choice-1])+10*"-")
            print(f"Original Data: {dataset.data}")
            print(f"Position(s)  : {eval(f'dataset.{self.options[choice-1]}({val})')}")

        input("...")
        self.show_menu()
        
    def clear_screen(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

if __name__ == "__main__":
    menu = Menu()