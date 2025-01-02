# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Formula to convert Celsius to Fahrenheit
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Formula to convert Fahrenheit to Celsius
    return (fahrenheit - 32) * 5/9

# Main function to convert temperature based on user input
def convert_temperature():
    # Displaying a welcome message
    print("Welcome to Cognifyz Technologies Temperature Converter!")
    
    # Get the temperature value from the user and convert it to float
    temp_value = float(input("Enter the temperature value: "))
    
    # Get the unit of measurement from the user, making it case-insensitive
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

    # Convert the temperature based on the unit entered by the user
    if unit == "C":
        # Convert Celsius to Fahrenheit and print the result
        converted_temp = celsius_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is equal to {converted_temp:.2f}°F.")
    elif unit == "F":
        # Convert Fahrenheit to Celsius and print the result
        converted_temp = fahrenheit_to_celsius(temp_value)
        print(f"{temp_value}°F is equal to {converted_temp:.2f}°C.")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Call the function to run the program
convert_temperature()
