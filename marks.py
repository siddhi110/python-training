m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
print("Total marks=",total)
print("Percentage:" ,percentage)
if percentage >= 90:
    print("Result:Distination")
elif percentage >= 80:
    print("Result:First class")
elif percentage >= 70:
    print("Result:pass")
else:
    print("Result:fail")
