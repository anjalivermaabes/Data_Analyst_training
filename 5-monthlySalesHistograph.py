import matplotlib.pyplot as plt
salaries=[
    20000,25000,30000,12000,
    40000,42000,54000,48000,
    37000,10000,63000,51000
]
plt.figure(figsize=(8,5))
plt.hist(
    salaries,
    bins=5,
    color="skyblue",
    edgecolor="black"
)
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("no. of employee")
plt.show()