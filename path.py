from typing import List

from costmaps import Map
import random


class Path:
    cities: List[int] = []
    cost: List[int] = 0
    map = Map.get_map(0)

    def __init__(self, cities2=None):

        if cities2 is None:
            cities2 = []
        self.set_cities(cities2.copy())

    def set_cities(self, cities2):
        self.cities = cities2.copy()
        self.commit()

    def commit(self):

        self.cost = 0

        for city in self.cities:
            if city == self.cities[-1]:
                break
            else:
                self.cost += Path.map[city][self.cities[self.cities.index(city) + 1]]

    @staticmethod
    def set_map(map):
        Path.map = map

    @staticmethod
    def get_random_path():
        cities = []

        length = len(Path.map)
        for i in range(length):
            cities.append(i)

        random.shuffle(cities)

        p = Path(cities)
        p.commit()

        return p
