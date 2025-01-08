class StringOperations:
    def __init__(self, string):
        self.string = string

    def is_palindrome(self):
        """Checks if the string is a palindrome."""
        return self.string.lower() == self.string[::-1].lower()

    def count_vowels(self):
        """Counts the number of vowels in the string."""
        vowels = "aeiouAEIOU"
        count = 0
        for char in self.string:
            if char in vowels:
                count += 1
        return count

    def reverse_string(self):
        """Reverses the string."""
        return self.string[::-1]

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("a. Check Palindrome")
        print("b. Count Vowels")
        print("c. Reverse String")
        print("d. Exit")
        choice = input("Enter your choice: ")

        if choice == 'a':
            string = input("Enter a string: ")
            obj = StringOperations(string)
            if obj.is_palindrome():
                print(f"{string} is a palindrome.")
            else:
                print(f"{string} is not a palindrome.")

        elif choice == 'b':
            string = input("Enter a string: ")
            obj = StringOperations(string)
            vowel_count = obj.count_vowels()
            print(f"Number of vowels in {string}: {vowel_count}")

        elif choice == 'c':
            string = input("Enter a string: ")
            obj = StringOperations(string)
            reversed_string = obj.reverse_string()
            print(f"Reversed string: {reversed_string}")

        elif choice == 'd':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
