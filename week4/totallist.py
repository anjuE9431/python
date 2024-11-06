
input_string = input("Enter numbers separated by spaces: ")

numbers = [int(x) for x in input_string.split()]


total = sum(numbers)



print("The sum of all items in the list is:", total)
