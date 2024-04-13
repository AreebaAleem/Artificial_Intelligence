# use loops to accept 5 values from the user and store them in a list and display the list.

list = []

for i in range(5):
    value = input(f"Enter value {i + 1}: ")
    list.append(value)

print("List:", list)
