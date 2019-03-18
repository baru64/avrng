import math
from avrng import Avrng
import matplotlib.pyplot as plt

def entropy(n):
    result = 0
    size = len(n)
    for i in n:
        result += ((i/size)*math.log2(i/size))
    return -result

if __name__ == "__main__":
    # todo histogram, entropia, kompresja
    trng = Avrng(0,0)
    x = [trng.get_byte() for i in range(100)]
    print("Entropia: {}".format(entropy(x)))
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()
    