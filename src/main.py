import os
import sys
from OPTFF import OPTFFCache
from FIFO import FIFOCache
from LRU import LRUCache


def read_input(filename):
    with open(f"./{filename}", "r") as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    return k, m, requests

def build_caches(k, requests):
    fifo_cache = FIFOCache(k)
    lru_cache = LRUCache(k)
    optff_cache = OPTFFCache(k, requests)

    for r in requests:
        fifo_cache.put(r, r)
        lru_cache.put(r, r)
        optff_cache.put(r, r)

    return fifo_cache, lru_cache, optff_cache

def write_output(fifo_cache, lru_cache, optff_cache):
    filename_raw = "./" + sys.argv[1]
    output_file = filename_raw.replace("input/", "output/").replace(".in", ".out")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        f.write(f"FIFO  : {fifo_cache.misses}\n")
        f.write(f"LRU   : {lru_cache.misses}\n")
        f.write(f"OPTFF : {optff_cache.misses}\n")
    print("Output written to", output_file)

if __name__ == "__main__":
    # Read capacity, request count, and requests
    k, m, requests = read_input(sys.argv[1])

    # Build the caches
    fifo_cache, lru_cache, optff_cache = build_caches(k, requests)

    # Write output to the output dir
    write_output(fifo_cache, lru_cache, optff_cache)









