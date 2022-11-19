# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]
res = 0
for i in numbers:
    if i % 2 == 0:
        res += i

print(f'Sum of all the even numbers in list = {res}')