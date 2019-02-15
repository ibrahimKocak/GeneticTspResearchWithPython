import random


def swap(path):
    length = len(path.cities)
    city1 = random.randrange(length)

    while True:
        city2 = random.randrange(length)

        if city1 != city2:
            break

    path.cities[city1], path.cities[city2] = path.cities[city2], path.cities[city1]
    path.commit()


def swap_neighbor(path):        #technically provides a more local search than normal swap search
    length = len(path.cities) - 1
    city1 = random.randrange(length)
    city2 = city1 + 1

    path.cities[city1], path.cities[city2] = path.cities[city2], path.cities[city1]
    path.commit()


def reverse(path):
    length = len(path.cities)
    city1 = random.randrange(length)

    while True:
        city2 = random.randrange(length)

        if city1 != city2:
            break

    if city1 > city2:
        city1, city2 = city2, city1

    path.cities[city1:city2+1] = reversed(path.cities[city1:city2+1])

    path.commit()


def insert(path):               #less efective from swap
    length = len(path.cities)
    city1 = random.randrange(length)

    while True:
        city2 = random.randrange(length)

        if city1 != city2 and city1 != city2+1 and city1+1 != city2:
            break

    if city1 < city2:
        path.cities.insert(city1+1, path.cities[city2])
        del path.cities[city2+1]

    if city1 > city2:
        path.cities.insert(city2+1, path.cities[city1])
        del path.cities[city1+1]

    path.commit()


