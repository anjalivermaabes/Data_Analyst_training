import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(42)
n = 40
df = pd.DataFrame({
    "Student_ID": range(1, n + 1),
    "Branch": np.random.choice(["CSE", "ECE", "ME", "CE"], n),
    "Study_Hours": np.round(np.random.uniform(1, 8, n), 1),
    "Attendance": np.random.randint(55, 100, n),
})
df["Marks"] = np.clip(
    np.round(30 + 5 * df["Study_Hours"] + 0.2 * df["Attendance"] + np.random.normal(0, 6, n)),
    0, 100
).astype(int)

df.head()



# TASK 1
# Task 1: Grading function
# •	Write a function get_grade(marks) that returns "A" for 75 and above, "B" for 60 to 74, "C" for 40 to 59, and "F" below 40.
# •	Add a Grade column to df using apply().
# •	Show how many students got each grade using value_counts().

def get_grade(marks):
  if marks >=75:
   return "A"
  elif marks >= 60:
   return "B"
  elif marks >= 40:
   return "C"
  else :
   return "F"

# 1 
print (get_grade (50))
print (get_grade (80))
print (get_grade (10))
# 2
df["Grade"] = df["Marks"].apply(get_grade)
print(df[["Student_ID", "Marks", "Grade"]].head())
# 3
print(df["Grade"].value_counts())


# TASK 2
# Task 2: Comprehensions and lambda
# •	Using a list comprehension, create a list of marks of students whose attendance is below 75.
# •	Using filter() and a lambda, get all marks above 70.
# •	Using map() and a lambda, add 5 grace marks to every student's marks (the maximum must stay 100).

low_attendance_marks = {
    marks
    for marks, attendance in zip(df["Marks"], df["Attendance"])
    if attendance < 75
}
# 1
print(low_attendance_marks)
# 2
high_marks = list(filter(lambda x: x > 70, df["Marks"]))
print(high_marks)
# 3
grace_marks = list(map(
    lambda marks: min(marks + 5, 100),
    df["Marks"]
))
print("Grace marks:", grace_marks)


# TASK 3
# Task 3: Flexible functions
# •	Write a function summary(*values, round_to=2) that accepts any number of values and returns a dictionary with the count, minimum, maximum and average.
# •	Test it with summary(10, 20, 30) and with summary(*df["Marks"]).

def summary(*values, round_to=2):
    if not values:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "average": None
        }

    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "average": round(
            sum(values) / len(values), round_to
        )
    }

print(summary(10, 20, 30))
print(summary(*df["Marks"]))


# TASK 4
# Task 4: Safe file handling
# •	Save df to a file named students.csv using to_csv(index=False).
# •	Write a function load_data(filename) that reads a CSV file using try and except. If the file is not found, it should print a friendly message instead of crashing.
# •	Test it once with the correct file name and once with a wrong name.

df.to_csv("students.csv", index=False)

def load_data(filename):
    try:
        data = pd.read_csv(filename)
        print("File loaded successfully")
        return data

    except FileNotFoundError:
        print("File not found. Check the filename.")
        return None

correct_file = load_data("students.csv")
wrong_file = load_data("wrong.csv")

print(correct_file.head())


# TASK 5
# Task 5: Grouping with Pandas
# •	Find the average Marks and average Study_Hours for each Branch using groupby().
# •	Which branch has the highest average marks?
# •	Display the top 5 students by marks using sort_values().

branch_avg = df.groupby("Branch")[
    ["Marks", "Study_Hours"]
].mean()

print(branch_avg)

highest_branch = branch_avg["Marks"].idxmax()
print("Highest average marks:", highest_branch)

top_5 = df.sort_values(
    by="Marks", ascending=False
).head(5)

print(top_5)


# TASK 6
# Task 6: Fast calculations with NumPy
# •	Convert the Marks column to a NumPy array.
# •	Calculate the z-score of every student using the formula (marks − mean) ÷ standard deviation. Do not use a loop.
# •	How many students have a z-score greater than 1?


marks = df["Marks"].to_numpy()

mean = np.mean(marks)
std = np.std(marks)

z_scores = (marks - mean) / std

print("Z-scores:", z_scores)
print("Students with Z > 1:", np.sum(z_scores > 1))


# TASK 7
# Task 7: Describing the marks
# •	Calculate the mean, median, mode, variance, standard deviation, minimum and maximum of Marks.
# •	Find Q1, Q3 and the IQR. Use the rule lower limit = Q1 − 1.5 × IQR and upper limit = Q3 + 1.5 × IQR to check for outliers.
# •	In 2 to 3 lines, explain what the mean, median and standard deviation tell you about the class.

marks = df["Marks"]

print("Mean:", marks.mean())
print("Median:", marks.median())
print("Mode:", marks.mode().tolist())
print("Variance:", marks.var())
print("Standard Deviation:", marks.std())
print("Minimum:", marks.min())
print("Maximum:", marks.max())

q1 = marks.quantile(0.25)
q3 = marks.quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df[
    (df["Marks"] < lower) |
    (df["Marks"] > upper)
]

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Outliers:", outliers)


# TASK 8
# Task 8: Correlation
# •	Find the correlation of Marks with Study_Hours and of Marks with Attendance using .corr().
# •	Which relationship is stronger? Is it positive or negative? Explain in simple words.
# •	In one line, explain why a high correlation does not prove that one thing causes the other.

study_corr = df["Marks"].corr(df["Study_Hours"])
attendance_corr = df["Marks"].corr(df["Attendance"])

print("Study Hours Correlation:", study_corr)
print("Attendance Correlation:", attendance_corr)

if abs(study_corr) > abs(attendance_corr):
    print("Study Hours has a stronger relationship.")
else:
    print("Attendance has a stronger relationship.")


# TASK 9
# Task 9: Confidence interval
# •	Calculate a 95% confidence interval for the average marks using stats.t.interval().
# •	Write one sentence explaining what this interval means.

mean_marks = df["Marks"].mean()
sem = stats.sem(df["Marks"])

confidence_interval = stats.t.interval(
    confidence=0.95,
    df=len(df["Marks"]) - 1,
    loc=mean_marks,
    scale=sem
)

print("95% Confidence Interval:", confidence_interval)


# TASK 10
# Task 10: Hypothesis test on one group
# The department claims that the average marks of students is 60.
# •	Write the null hypothesis (H0) and the alternative hypothesis (H1).
# •	Run a one-sample t-test using stats.ttest_1samp(df["Marks"], 60).
# •	Using a significance level of 0.05, state whether you reject H0 and what it means for the claim.

t_stat, p_value = stats.ttest_1samp(
    df["Marks"], 60
)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject H0")
    print("Average marks differ significantly from 60.")
else:
    print("Fail to reject H0")
    print("Insufficient evidence against the claim.")


#     TASK 11
#     Task 11: Hypothesis test on two groups
# •	Compare the marks of CSE students and ECE students using stats.ttest_ind().
# •	Write H0 and H1, report the p-value, and state your conclusion at the 0.05 level in plain English.

cse_marks = df[df["Branch"] == "CSE"]["Marks"]
ece_marks = df[df["Branch"] == "ECE"]["Marks"]

t_stat, p_value = stats.ttest_ind(
    cse_marks, ece_marks
)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject H0")
    print("Significant difference between CSE and ECE.")
else:
    print("Fail to reject H0")
    print("No statistically significant difference detected.")



# TASK 12
# Task 12: In 4 to 5 lines, summarise what your analysis shows about the marks of these students and which factor seems to matter most.

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("Study Correlation:",
      df["Marks"].corr(df["Study_Hours"]))

print("Attendance Correlation:",
      df["Marks"].corr(df["Attendance"]))