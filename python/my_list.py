# Create an empty list
my_list = []

# Appends elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at 1st index
my_list.insert(1, 15)

# Extend my_list with another list
new_list = [50, 60, 70]
my_list.extend(new_list)

# Remove the last element from my_list
my_list.pop()

# Sort my_list
sorted_list = sorted(my_list)

# Find and print the index of the value 30 in my_list
index30 = sorted_list.index(30)
print("Index of 30 in my_list:", index30)

# Print the final content of my_list
print("Final content of my_list:", sorted_list)
