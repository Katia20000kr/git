amount = input("Give amount:")
amount = int(amount)

vat_rate = input("Give vat rate:")
vat_rate = int(vat_rate)

vat = amount * (vat_rate/100)
total_payment = amount + vat

print(f"the total payment is : {total_payment: .2f}")