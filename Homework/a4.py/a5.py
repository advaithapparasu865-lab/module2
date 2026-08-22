def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number_of_terms = int(input("How many terms do you want? "))

if number_of_terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci sequence:")

    for position in range(number_of_terms):
        print(fibonacci(position), end=" ")