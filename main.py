from path import Path
from mutation import swap,reverse,insert
import time

cities = [0, 1, 2, 3]
p = Path(cities)

start = time.time()

for i in range(1000000):
    reverse(p)

end = time.time()

print("time: ", end - start)

p.init_random_path()