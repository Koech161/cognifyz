import re


def check_password_strength(password):

    # check if password length
    if len(password) < 8:
        return 'Password is too short. It must be at least 8 characters long.'
    
    # Check if password contain at least one uppercase letter

    if not re.search(r'[A-Z]', password):
        return 'Password must contain at least one uppercase letter.'
    
    # check if password contain at least one lowercase letter

    if not re.search(r'[a-z]', password):
        return 'password must contain at least one lowercase letter.'
    
    # check if password contain at least one number
     
    if not re.search(r'[0-9]', password):
        return 'password must contain at least one number.'
    
    # Check if password contain at least one special character

    if not re.search(r'[!$&*@?%]', password):
        return 'password must contain  at least one special character (!, @, $, %, &, *, ?).'
    
    # if all conditions are met , the password is strong

    return 'Password is strong.'

inp = input('Enter your password: ')
result = check_password_strength(inp)

print(result)