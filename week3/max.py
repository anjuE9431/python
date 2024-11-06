
user_input = input("Enter a list of numbers separated by spaces: ")
input_list = list(map(int, user_input.split())) 


if input_list:
    max_value = max(input_list)     
    min_value = min(input_list)       
    length = len(input_list)          
    reversed_list = input_list[::-1]  
    total_sum = sum(input_list)      
    sorted_list = sorted(input_list)   

   
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")
    print(f"Length of the list: {length}")
    print(f"Reversed list: {reversed_list}")
    print(f"Sum of the values: {total_sum}")
    print(f"Sorted list: {sorted_list}")
else:
    print("The list is empty.")
