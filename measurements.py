import math
import subprocess
import os
from avrng import Avrng
import numpy as np
import matplotlib.pyplot as plt

def entropy(n):
    result = 0
    p = hist(n)
    size = len(n)
    for _, i in p.items():
        if i:
            result += ((i/size)*math.log2(i/size))
    return -result

def hist(n):
    p = dict((value, 0) for value in range(256))
    for v in n:
        p[v] += 1
    return p

SIZE = 10000
FILENAME = 'random.bin'

if __name__ == "__main__":
    trng = Avrng(0,0)
    x = np.array([trng.get_byte() for i in range(SIZE)], dtype='uint8')

    print("Entropy: {}".format(entropy(x)))

    plt.figure()
    histogram = hist(x)
    plt.bar(histogram.keys(), histogram.values(), width=1, color='g')
    plt.title("Histogram of random bytes")
    plt.grid(True)
    
    plt.figure()
    x.tofile(FILENAME)
    subprocess.run(["xz", "-kf", FILENAME])
    subprocess.run(["gzip", "-kf", FILENAME])
    if os.path.isfile(FILENAME + ".zip"):
        os.remove(FILENAME + ".zip")
    os.system("7z a -tzip " + FILENAME + ".zip " + FILENAME + " > /dev/null")
    
    compression_data = dict()
    compression_data['uncompressed'] = os.path.getsize(FILENAME)
    compression_data['xz (LZMA)'] = os.path.getsize(FILENAME + '.xz')
    compression_data['gzip (LZ77)'] = os.path.getsize(FILENAME + '.gz')
    compression_data['zip'] = os.path.getsize(FILENAME + '.zip')

    print(compression_data)
    plt.bar(compression_data.keys(), compression_data.values())
    plt.title("File size")
    plt.grid(True)
    plt.show()
