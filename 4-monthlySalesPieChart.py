import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20000, 10000, 58000, 45000, 80640, 94000]

plt.pie(sales, labels=months, autopct="%1.1f%%", startangle=90)
plt.title("Monthly Sales Distribution")
plt.show()