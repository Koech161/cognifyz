import re

# define a function to check if email is valid
def valid_email(input_email):
    #  Define a regular expression pattern for a valid email address
    email_pattern = r'^[a-zA-Z0-9_+-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # check if the email matches the pattern
    # use if statement to check condition
    if re.match(email_pattern, input_email):
        return True
    else:
        return False 
# usage
inp_email = input('Enter email to check: ')
result = valid_email(inp_email)
print(result)   
    
