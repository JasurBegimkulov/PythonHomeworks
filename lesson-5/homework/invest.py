def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"Year {year}: ${amount:.2f}")

initial_amount = float(input("The initial amount: "))
annual_rate = float(input("The annual rate of return : "))
investment_years = int(input("The number of years: "))

invest(initial_amount, annual_rate, investment_years)