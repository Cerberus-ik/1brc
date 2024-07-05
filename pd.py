import timeit
import pandas as pd

def main() -> None:
    df = pd.read_csv("measurements.txt", sep=";", names=["city", "temp"])
    df["temp"] = df["temp"].astype(float)
    df = df.groupby("city").agg(min_temp=("temp", "min"), max_temp=("temp", "max"), avg_temp=("temp", "mean"), count=("temp", "count"))
    print(df)

execution_time = timeit.timeit(main, number=1)
print(f"Execution time: {execution_time} seconds")