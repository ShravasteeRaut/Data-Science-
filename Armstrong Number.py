num_str = input("Enter a number: ")
num = int(num_str)
power = len(num_str)

total = 0

for digit in num_str:
    total += int(digit) ** power

if total == num:
    print(num, "is an Armstrong number!")
else:
    print(num, "is NOT an Armstrong number.")