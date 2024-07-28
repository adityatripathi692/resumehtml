def rent_calculator():
    print("Welcome to the Rent Calculator!")

    try:
        # Get the basic rent amount
        rent = float(input("Enter the monthly rent amount: $"))

        # Get the utilities costs
        utilities = float(input("Enter the monthly utilities cost (electricity, water, etc.): $"))

        # Get the internet cost
        internet = float(input("Enter the monthly internet cost: $"))

        # Get the other expenses
        other_expenses = float(input("Enter the other monthly expenses: $"))

        # Calculate the total monthly cost
        total_cost = rent + utilities + internet + other_expenses

        # Print the result
        print(f"\nThe total monthly rent cost is: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Call the rent calculator function
rent_calculator()
