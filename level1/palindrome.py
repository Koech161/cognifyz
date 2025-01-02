def is_palindrome(s):

    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

input_str = input('Enter a string to check if is a palindrome: ')

if is_palindrome(input_str):

    print(f'{input_str} is a palindrome.')
    
else:
    print(f'{input_str} is not a palindrome.')    