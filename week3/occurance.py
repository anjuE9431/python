def count_a_occurrences(names):
    count = 0
    for name in names:
        count += name.lower().count('a')  
    return count
user_input = input("Enter first names separated by commas: ")
first_names = [name.strip() for name in user_input.split(',')] 
total_a_count = count_a_occurrences(first_names)


print(first_names)
print(f"Total occurrences of 'a' in the names: {total_a_count}")
