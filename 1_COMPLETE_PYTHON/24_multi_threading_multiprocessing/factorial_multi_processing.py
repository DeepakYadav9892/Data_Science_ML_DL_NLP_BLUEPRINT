"""
Docstring for 24_multi_threading_multiprocessing.factorial_multi_processing

Real world example: Multiprocessing for CPU bound tasks scenario:
Factorial calculation

Factorial calculations, especially for large numbers, involve significant
computational work. Multiprocessing can be used to distribute the workload
across multiple CPU cores, improving performance.
"""

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer to string conversion
sys.set_int_max_str_digits(10000)

# Function to compute factorial of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} computed")
    return result

if __name__ == "__main__":

    numbers = [5000, 6000, 7000]

    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print("Results received")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
