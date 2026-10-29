
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# TASK - 1
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 20, 24, 22]

plt.plot(months, sales, marker="o", color="green")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

# #TASK -2
tips = sns.load_dataset("tips")

avg_tip = tips.groupby("day")["tip"].mean().reindex(
    ["Thur", "Fri", "Sat", "Sun"]
)

plt.bar(avg_tip.index, avg_tip.values, color="skyblue")

plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip ($)")
plt.grid(axis="y")

plt.show()

highest_day = avg_tip.idxmax()
highest_tip = avg_tip.max()

print("Day with the highest average tip:", highest_day)
print("Highest average tip: $", round(highest_tip, 2))


#TASK - 3
tips = sns.load_dataset("tips")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(tips["total_bill"], bins=10, color="skyblue", edgecolor="black")
axes[0].set_title("Distribution of Total Bill")
axes[0].set_xlabel("Total Bill ($)")
axes[0].set_ylabel("Frequency")

axes[1].scatter(tips["total_bill"], tips["tip"], color="green")
axes[1].set_title("Total Bill vs Tip")
axes[1].set_xlabel("Total Bill ($)")
axes[1].set_ylabel("Tip ($)")

plt.tight_layout()

plt.savefig("tips_plots.png", dpi=150)

plt.show()

#TASK - 4


tips = sns.load_dataset("tips")

# Create two charts in one figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Count plot: Number of customers on each day
sns.countplot(data=tips, x="day", ax=axes[0], color="skyblue")
axes[0].set_title("Number of Customers by Day")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Number of Customers")

# Bar plot: Average bill on each day
sns.barplot(data=tips, x="day", y="total_bill", ax=axes[1], color="lightgreen")
axes[1].set_title("Average Bill by Day")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Average Total Bill ($)")

plt.tight_layout()
plt.show()

# Find the day with the most customers
customer_count = tips["day"].value_counts()
print("Day with the most customers:", customer_count.idxmax())

# Find the day with the highest average bill
avg_bill = tips.groupby("day")["total_bill"].mean()
print("Day with the highest average bill:", avg_bill.idxmax())
print("Highest average bill: $", round(avg_bill.max(), 2))



