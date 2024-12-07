from time import perf_counter
import numpy as np
from numcodecs import lz4

if __name__ == "__main__":

    np.random.seed(0)

    arr = np.random.random(25_000_000)  # 200MB

    time_start = perf_counter()

    for _ in range(100):
        enc = lz4.compress(arr)

    time_end = perf_counter()
    time_duration = time_end - time_start
    print(f'Took {time_duration:.3f} seconds')