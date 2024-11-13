amount = input("Give amount")
vat_rate = input("Give vat rate")

vat_amount = amount * (vat_rate / 100)

total_payment = amount + vat_amount

print("Total payment")