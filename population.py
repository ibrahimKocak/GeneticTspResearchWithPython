from typing import List

from path import Path
from crossingover import get_children
from mutation import swap, swap_neighbor, insert, reverse
import time
import random


class Population:
    parents: List[Path] = []
    children: List[Path] = []
    parents_length = 0

    def __init__(self, parent_count: int):  # Creating (parent_count) times parent and (parent_count x 2) times children
        self.parents = []
        self.children = []
        self.parents_length = parent_count

        for i in range(self.parents_length):
            self.parents.append(Path.get_random_path())

        self.print_paths(True, False)

    def print_paths(self, is_print_parents: bool, is_print_children: bool):

        if is_print_parents:
            print("parents:")
            for i in range(self.parents_length):
                print(f"{i:02d}", self.parents[i].cities, "cost: ", self.parents[i].cost)
            print("\n")

        if is_print_children:
            print("children:")
            for i in range(len(self.children)):
                print(f"{i:02d}", self.children[i].cities, "cost: ", self.children[i].cost)
            print("\n")

    def iteration(self, iteration_count):

        for i in range(iteration_count):
            self.children.clear()
            self.children.extend(get_children(self.parents))

    def create_new_children(self):

        self.children.clear()
        length = int(self.parents_length / 2)
        for i in range(length):
            self.children.extend(get_children(self.parents[2*i], self.parents[2*i+1]))

        if self.parents_length % 2 == 1:
            for i in range(int(len(get_children(self.parents[0], self.parents[0])) / 2)):
                self.children.append(Path.get_random_path())

    def select_new_parents(self):
        for i in range(self.parents_length):
            if self.children[i].cost < self.parents[i].cost:
                is_new = True
                for j in range(self.parents_length):
                    if self.children[i].cities == self.parents[j].cities:
                        is_new = False
                        break
                if is_new:
                    self.parents[i].set_cities(self.children[i].cities)

    def get_mutation_children(self):
        for i in range(len(self.children)):
            swap(self.children[i])


start = time.time()

pop0 = Population(10)

for i in range(200000):
    random.shuffle(pop0.parents)
    pop0.create_new_children()
    pop0.select_new_parents()
    pop0.get_mutation_children()
    pop0.select_new_parents()
    #pop0.print_paths(True, True)

pop0.print_paths(True, True)

end = time.time()
print("time: ", end - start)
