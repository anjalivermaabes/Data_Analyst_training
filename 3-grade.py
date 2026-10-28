grade = int(input("Enter the grade: "))
if grade > 100:
    print(f"The grade is invalid :: {grade}")
elif grade >= 90:
    print(f"The grade is A :: {grade}") 
elif grade >= 80:
    print(f"The grade is B :: {grade}")
elif grade >= 70:
    print(f"The grade is C :: {grade}") 
elif grade >= 60:
    print(f"The grade is D :: {grade}")
else:
    print(f"The grade is F :: {grade}")