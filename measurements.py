import math
from avrng import Avrng
import matplotlib.pyplot as plt

def entropy(n, r):
    result = 0

    p = dict((value, 0) for value in range(256))
    for v in n:
        p[v] += 1

    size = len(p)
    for _, i in p.items():
        if i:
            print(i)
            result += ((i/r)*math.log2(i/r))
    return -result

if __name__ == "__main__":
    trng = Avrng(0,0)
    rng = 10000
    x = [trng.get_byte() for i in range(rng)]
    # entropia pijana lub niespełna rozumu
    print("Entropia: {}".format(entropy(x, rng)))
    # naprawić histogram
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()
    # TODO kompresja
