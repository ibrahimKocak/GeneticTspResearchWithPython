from costmaps import get_map
import random


class Path:
    cities = []
    cost = 0
    costMap = []

    def __init__(self, cities2):

        self.costMap = get_map(0)
        self.set_cities(cities2)

    def set_cities(self, cities2):
        self.cities = cities2
        self.calculate_result()

    def init_random_path(self):
        self.cities = []

        for i in range(len(self.costMap)):
            self.cities.append(i)

        random.shuffle(self.cities)
        self.calculate_result()

    def calculate_result(self):

        self.cost = 0

        for city in self.cities:
            if self.cities.index(city) == len(self.cities) - 1:
                break
            else:
                self.cost += self.costMap[city][self.cities[self.cities.index(city) + 1]]

