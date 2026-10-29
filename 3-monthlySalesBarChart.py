import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

region = ["North", "South", "East", "West"]

sales_data = [10000, 10500, 200000, 25000]

plt.bar(region, sales_data, color="blue")

plt.title("Sales Data by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")

plt.grid(axis="y")
plt.show()