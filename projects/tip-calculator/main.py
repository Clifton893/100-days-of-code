#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# My solution: 

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? (Don't type '%') "))
people = int(input("How many people are splitting the bill? "))
bill_with_tip = tip / 100 * total_bill + total_bill
each_person_pays = round(bill_with_tip / people, 2)

print(f"Each person pays: ${each_person_pays}")





# Official solution (note how it's cleaner than mine):

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)

# #FAQ: How to round to 2 decimal places?
# #https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

# print(f"Each person should pay: ${final_amount}")
