num = int(input("Enter the number: "))
sum = 0
for i in range(num):
        inp = float(input(f"Enter value {i + 1}: "))
        sum += inp
print(f"The sum of the {num} numbers is: {sum}")