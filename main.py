print("Welcome to the Tip Calculator")
total_bill = int(input("What is the total bill? "))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
amount_of_people = int(input("How many people to split the bill? "))

bill_with_tip = (tip_amount / 100) * total_bill + total_bill
bill_per_person = bill_with_tip / amount_of_people
total_amount = round(bill_per_person, 2)

print(f"Each person will pay: {total_amount}")