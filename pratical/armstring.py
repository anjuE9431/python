def get_number():
  """
  Gets a number from the user as input.

  Returns:
    The entered number as an integer.
  """
  while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():  # Check if the input consists only of digits
      return int(user_input)
    else:
      print("Invalid input. Please enter an integer.") 

def is_armstrong_number(num):
  """
  Checks if the given number is an Armstrong number.

  Args:
    num: The number to be checked.

  Returns:
    True if the number is an Armstrong number, False otherwise.
  """
  temp = num
  sum_of_powers = 0
  num_digits = len(str(num))

  while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

  return num == sum_of_powers

# Get the number from the user
number = get_number()

# Check if it's an Armstrong number
if is_armstrong_number(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")
