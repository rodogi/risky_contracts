#!/usr/local/bin python3

""" Multi-threading the calculation of similarity between company names.

Returns
-------
matrix: numpy.save, a binary file.
"""

import sys
import itertools
import multiprocessing as mp
from mpi4py import MPI
from fuzzywuzzy import fuzz
import time


def similarity(pair, threshold=100):
    """Get the distance in meters between a and b"""
    i = pair[0]
    j = pair[1]

    # strings
    s_i = companies[i]
    s_j = companies[j]

    if fuzz.partial_token_set_ratio(s_i, s_j) >= threshold:
        matrix.setdefault(i, [])
        matrix[i].append(str(j))
    pass


if __name__ == '__main__':
    # Calculate bounds (rows) per thread
    path_companies = ("/home/rdora/declaranet/data/pre-process/"
                      "list_companies.txt")
    with open(path_companies, 'r') as f:
        # List of strings of size ~600k
        companies = f.read().splitlines()

    n = len(companies)
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    chunk = int(n / size)

    lower_bound = rank * chunk  # El primero es 0, segundo chunk, ...
    upper_bound = (rank * chunk) + chunk
    if rank == size - 1:
        chunk = n - (chunk * rank)
        upper_bound = n
    print("Lower Bound:", lower_bound,
          "Upper bound:", upper_bound, "rank:", rank)

    print(f"There are {chunk:,} companies to parse")

    # Aqui se van a poner los valores
    matrix = dict()

    # itera dos veces en la lista companies
    # size n * (n-1) / 2
    print(f"Iterando {chunk * (chunk - 1) / 2:,} veces")
    # Range [lowe_bound, upper_bound) semi-closed range
    pairs = itertools.combinations(range(lower_bound, upper_bound), 2)
    print(f"pairs is size {sys.getsizeof(pairs)/(1024 * 1024)}MB")

    # Main for loop
    for pair in pairs:
        similarity(pair)

    with open(f"/home/rdora/declaranet/data/pre-process/similarity{rank}.txt", "w") as f:
        nlines = 0
        for key in matrix:
            line = matrix[key]
            nlines += len(line)
            f.write(f"{key} ")
            f.write(" ".join(line))
            f.write("\n")
        print(f"There are {nlines} pairs of strings that match 100%")
