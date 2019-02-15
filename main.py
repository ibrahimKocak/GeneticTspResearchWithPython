from path import Path
from mutation import swap,reverse,insert
import time

p = Path.get_random_path()

print(p.cities, p.cost)

start = time.time()

for i in range(1000):
    swap(p)
    print(p.cities, p.cost)

end = time.time()

print("time: ", end - start)

