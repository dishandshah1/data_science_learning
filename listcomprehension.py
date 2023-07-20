def divisor(num1):
    try:
        num1 = int(num1)  # Convert the input to an integer
        if num1 < 2:  # Check if the number is less than 2
            print("Number should be greater than 1")
        else:
            # Use a list comprehension to generate the divisors
            divisors = [i for i in range(2, num1) if num1 % i == 0]
            # Print each divisor
            for divisor in divisors:
                print(divisor)
    except ValueError:  # Raised when the input cannot be converted to an integer
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:  # Catch any other exceptions
        print("An error occurred:", str(e))

try:
    number = input("Enter the number: ")
    divisor(number)
except Exception as e:  # Catch any exceptions that occur while getting input
    print("An error occurred:", str(e))
