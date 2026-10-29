
import matplotlib.pyplot as plt

it_salary = [40000, 45000, 50000, 55000, 70000]
hr_salary = [30000, 35000, 40000, 42000, 45000]
finance_salary = [35000, 40000, 45000, 52000, 60000]

salary_data = [it_salary, hr_salary, finance_salary]

plt.figure(figsize=(8, 5))

plt.boxplot(
    salary_data,
    patch_artist=True,
    tick_labels=["IT", "HR", "Finance"]
)

plt.title("Salary Distribution by Department")
plt.ylabel("Salary ($)")
plt.grid(axis="y")

plt.show()
