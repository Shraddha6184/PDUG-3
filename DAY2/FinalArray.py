
my_list = []

n = int(input("How many elements do you want to add? "))

for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    my_list.append(element)

print("Final list:", my_list)
