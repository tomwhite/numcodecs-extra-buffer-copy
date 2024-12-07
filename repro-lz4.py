import hashlib
import numpy as np
from numcodecs import lz4

if __name__ == "__main__":

    np.random.seed(0)

    arr = np.random.random(25_000_000)  # 200MB

    # defaults
    enc = lz4.compress(arr)

    h = hashlib.new('sha256')
    h.update(enc)
    print(h.hexdigest())
