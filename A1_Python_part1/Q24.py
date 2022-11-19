# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if a>b and a>c:
    print(f"{a} is greatest.")
elif b>c:
    print(f"{b} is greatest.")
else:
    print(f"{c} is greatest.")