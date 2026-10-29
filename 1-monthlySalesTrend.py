import matplotlib.pyplot as plt
months = ["Jan", "Feb","Mar","Apr","May","Jun"]
sales = [1500, 2000, 1800, 2200, 2500, 3000]
plt.plot(months, sales, marker='o',color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.show()