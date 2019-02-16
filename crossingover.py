import random
from typing import List
import time
from path import Path


def get_template(count):
    template = []

    for i in range(count):
        template.append(random.random() < 0.5)

    return template


def get_children(path0: Path, path1: Path):
    children = [Path(), Path()]
    cities0 = []
    cities1 = []
    path0_cities = path0.cities.copy()
    path1_cities = path1.cities.copy()

    count = len(path0.cities)
    for i in range(count):
        cities0.append(-1)
        cities1.append(-1)

    template = get_template(count)

    for i in range(count):
        if template[i]:
            cities0[i] = path0.cities[i]
            path1_cities.remove(path0.cities[i])
            cities1[i] = path1.cities[i]
            path0_cities.remove(path1.cities[i])

    index = 0
    for i in range(count):
        if not template[i]:
            cities0[i] = path1_cities[index]
            cities1[i] = path0_cities[index]
            index += 1

    children[0].set_cities(cities0.copy())
    children[1].set_cities(cities1.copy())

    return children
