# accept 2 list from the user and display the joint

list1 = []
list2 = []

num1 = int(input("Enter the number of elements for the first list: "))
for i in range(num1):
    element = input(f"Enter element {i + 1} for the first list: ")
    list1.append(element)

num2 = int(input("Enter the number of elements for the second list: "))
for i in range(num2):
    element = input(f"Enter element {i + 1} for the second list: ")
    list2.append(element)

joint = list1 + list2
print("Joint list:", joint)
