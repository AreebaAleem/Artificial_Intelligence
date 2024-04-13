# use loops to accept 5 values from the user and store them in a list and display the sum of list.

list = []

for i in range(5):
    inp = float(input(f"Enter value {i + 1}: ")) 
    list.append(inp)
    
sum = sum(list)

print("List:", list)
print("Sum of the list:", sum)
