# Define the function to reverse a string
def reverse_string(input_string):
    # Initialize an empty string to hold the reversed string
    reverse_str = ""

    # Iterate over each character in the input string
    for char in input_string:
        # Prepend the current character to the reversed string
        reverse_str = char + reverse_str

    # Return the reversed string
    return reverse_str

# Define the input string to be reversed
input_str = 'Python'

# Call the reverse_string function and store the result in reversed_str
reversed_str = reverse_string(input_str)

# Print the reversed string
print(reversed_str)
