import timeit
from numba import njit


@njit
def main() -> None:
    results = {}
    with open("measurements.txt") as f:
        for line in f:
            city, temp = line.strip().split(";")
            temp = float(temp)
            if results.get(city) is None:
                results[city] = [100,-100,0,0]
            results[city][2] = results[city][2]  + temp
            if temp < results[city][0]:
                results[city][0] = temp
            if temp > results[city][1]:
                results[city][1] = temp
            results[city][3] += 1
    for city in results:
        print(f"City: {city}, Min: {results[city][0]}, Max: {results[city][1]} Avg: {results[city][2]/results[city][3]}")


execution_time = timeit.timeit(main, number=1)
print(f"Execution time: {execution_time} seconds")