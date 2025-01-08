string = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
modified_string = ""

for char in string:
  if char in vowels:
    vowel_count += 1
    modified_string += "#"
  else:
    modified_string += char

print(f"Number of vowels: {vowel_count}")
print("String after replacing vowels with '#':", modified_string)
