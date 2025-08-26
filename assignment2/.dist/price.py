#7. Write a program that will calculate the price for a quantity entered from the keyboard, given that the
#unit price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15 percent discount
#for qu antities over 50.


quantity = int(input("Enter quantity: "))
unit_price = 5
total_price = quantity * unit_price

if quantity > 50:
    discount = 0.15 * total_price
elif quantity > 30:
    discount = 0.10 * total_price
else:
    discount = 0
final_price = total_price - discount

print("Total price before discount: Rs.", total_price)
print("Discount applied: Rs.", round(discount, 2))
print("Final price to pay: Rs.", round(final_price, 2))
