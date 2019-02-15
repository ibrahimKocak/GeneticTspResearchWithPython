import random
from typing import List

from path import Path


def get_template(count):
    template = []

    for i in range(count):
        template.append(random.random() < 0.5)

    return template


def get_children(path0: Path, path1: Path, is_kill_weakens: bool = True):
    cities0 = path0.cities.copy()
    cities1 = path1.cities.copy()

    temp_cities = [cities1.copy(), cities0.copy(), cities1.copy(), cities0.copy()]
    children: List[List[int]] = []

    length = len(cities1)

    for i in range(4):
        children.append([])

    kid0 = []
    kid1 = []

    for i in range(length):
        if random.random() < 0.5:
            kid0.append(i)
        else:
            kid1.append(i)

    length = len(kid0)

    for i in range(length):
        children[0].append(cities0[kid0[i]])
        temp_cities[0].remove(cities0[kid0[i]])
        children[1].append(cities1[kid0[i]])
        temp_cities[1].remove(cities1[kid0[i]])

    length = len(kid1)

    for i in range(length):
        children[2].append(cities0[kid1[i]])
        temp_cities[2].remove(cities0[kid1[i]])
        children[3].append(cities1[kid1[i]])
        temp_cities[3].remove(cities1[kid1[i]])

    for i in range(length):
        children[0].insert(kid1[i], temp_cities[0].pop(0))
        children[1].insert(kid1[i], temp_cities[1].pop(0))

    length = len(kid0)

    for i in range(length):
        children[2].insert(kid0[i], temp_cities[2].pop(0))
        children[3].insert(kid0[i], temp_cities[3].pop(0))

    children: list[Path] = [Path(children[0]), Path(children[1]), Path(children[2]), Path(children[3])]

    if is_kill_weakens:
        children.sort(key=lambda x: x.cost)
        del children[-1]
        del children[-1]

    return children


