KM_TO_MILES=0.621371
CELSIUS_SCALE=9/5
FEHRENHEIT_OFFSET=32

def get_number(message):
    while True:
        user_input=input(message).strip()

        if user_input=="":
            print("Input cannot be empty. Please enter a number.")
            continue

        try:
            number=float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def addition():
    num1=get_number("Enter the first number: ")
    num2=get_number("Enter the second number: ")
    result=num1+num2
    print(f"The sum of {num1} and {num2} is {result}.")

def subtraction():
    num1=get_number("Enter the first number:")
    num2=get_number("Enter the second number:")
    result=num1-num2
    print(f"The difference between {num1} and {num2} is {result}.")

def multiplication():
    num1=get_number("Enter the first number:")
    num2=get_number("Enter the second number:")
    result=num1*num2
    print(f"The product of {num1} and {num2} is {result}.")

def division():
    num1=get_number("Enter the first number:")
    num2=get_number("Enter the second number:")
    if num2==0:
        print("Error: Division by zero is not allowed.")
        return
    result=num1/num2
    print(f"The quotient of {num1} divided by {num2} is {result}.")

def km_to_miles():
    km=get_number("Enter the distance in kilometers:")
    miles=km*KM_TO_MILES
    print(f"{km} kilometers is equal to {miles} miles.")

def celsius_to_fahrenheit():
    celsius=get_number("Enter the temperature in Celsius:")
    fahrenheit=celsius*CELSIUS_SCALE+FEHRENHEIT_OFFSET
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

def show_calculator_menu():
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back to Main Menu")

        choice=input("Enter your choice (1-5): ").strip()

        if choice=="1":
            addition()
        elif choice=="2":
            subtraction()
        elif choice=="3":
            multiplication()
        elif choice=="4":
            division()
        elif choice=="5":
            break
        else:
            print("Invalid choice. Please select 1 to 5.")

def show_convertor_menu():
    while True:
        print("\nUnit Convertor Menu:")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Back to Main Menu")

        choice=input("Enter your choice (1-3): ").strip()

        if choice=="1":
            km_to_miles()
        elif choice=="2":
            celsius_to_fahrenheit()
        elif choice=="3":
            break
        else:
            print("Invalid choice. Please select 1 to 3.")

def main():
    while True:
        print("\n=====Interactive Calculator and Unit Convertor=====")
        print("1. Calculator")
        print("2. Unit Convertor")
        print("3. Exit")

        choice=input("Enter your choice (1-3): ").strip()

        if choice=="1":
            show_calculator_menu()
        elif choice=="2":
            show_convertor_menu()
        elif choice=="3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 3.")

if __name__=="__main__":
    main()

