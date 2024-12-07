import numpy as np
from numcodecs import blosc
from numcodecs.blosc import Blosc

if __name__ == "__main__":
    arr = np.random.random(25_000_000)  # 200MB
    blosc.compress(arr, b'lz4', 5, Blosc.SHUFFLE)
