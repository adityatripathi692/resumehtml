def rent_calculator():
    print("Welcome to the Rent Calculator!")

    try:

        rent = float(input("Enter the monthly rent amount: rupees"))

        utilities = float(input("Enter the monthly utilities cost (electricity, water, etc.): rupees"))
        
        internet = float(input("Enter the monthly internet cost: rupees"))

        other_expenses = float(input("Enter the other monthly expenses: rupees"))

        people = float(input("Enter how many people are there:"))
        total_cost = rent + utilities + internet + other_expenses/prople
        
        print(f"\n Each person has to contribute : rupees{total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Call the rent calculator function
rent_calculator()
