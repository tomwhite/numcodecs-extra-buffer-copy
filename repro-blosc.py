import hashlib
import numpy as np
from numcodecs import blosc
from numcodecs.blosc import Blosc

if __name__ == "__main__":

    blosc.set_nthreads(1)  # ensure blosc is determinstic, see https://github.com/zarr-developers/zarr-python/discussions/1519 

    np.random.seed(0)

    arr = np.random.random(25_000_000)  # 200MB

    # defaults
    enc = blosc.compress(arr, b'lz4', 5, Blosc.SHUFFLE)

    h = hashlib.new('sha256')
    h.update(enc)
    print(h.hexdigest())
