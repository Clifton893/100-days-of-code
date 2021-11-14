# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? (Don't type '%') "))
people = int(input("How many people are splitting the bill? "))
bill_with_tip = tip / 100 * total_bill + total_bill
each_person_pays = round(bill_with_tip / people, 2)

print(f"Each person pays: ${each_person_pays}")
