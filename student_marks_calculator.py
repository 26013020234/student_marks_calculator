name = input("Enter student name: ")

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Pass")
else:
    print("Fail")