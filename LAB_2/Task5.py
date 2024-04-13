# have a list and input then search that number in the list

list = [10, 20, 30, 40, 50, 100]
search = int(input("Enter the number to search: "))

found = False
for num in list:
    if num == search:
        found = True
        break

if found:
    print(f"{search} found in the list")
else:
    print(f"{search} not found in the list")
