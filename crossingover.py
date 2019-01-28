from random import random
import time

def get_template(count):
    template = []

    for i in range(count):
        template.append(random() < 0.5)

    return template


def get_children(cities0: list, cities1: list):
    temp_cities = [cities1.copy(), cities0.copy(), cities1.copy(), cities0.copy()]
    children = []

    length = len(cities1)

    for i in range(4):
        children.append([None] * length)

    template = get_template(length)

    for i in range(length - 1, -1, -1):
        if template[i]:
            children[0][i] = cities0[i]
            temp_cities[0].remove(cities0[i])
            children[1][i] = cities1[i]
            temp_cities[1].remove(cities1[i])
        else:
            children[2][i] = cities0[i]
            temp_cities[2].remove(cities0[i])
            children[3][i] = cities1[i]
            temp_cities[3].remove(cities1[i])

    for i in range(length - 1, -1, -1):
        if template[i]:
            children[2][i] = temp_cities[2].pop()
            children[3][i] = temp_cities[3].pop()
        else:
            children[0][i] = temp_cities[0].pop()
            children[1][i] = temp_cities[1].pop()

    return children

c1 = [0, 1, 4, 3, 2]
c2 = [2, 4, 3, 1, 0]

start = time.time()

for j in range(100000):
    get_children(c1, c2)

end = time.time()

print("time: ", end - start)