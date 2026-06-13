#percentage homework
#first homework .Collect the price of an item and the percentage discount, then subtract the discounted price from the original price.
price = float(input("Enter the price of the item: "))
#percentage discount
discount_percentage = float(input("Enter the percentage discount: "))
#calculate the discount amount
discount_amount = (discount_percentage / 100) * price
#calculate the discounted price
discounted_price = price - discount_amount

#output
print(f"The current price of the item after removal of discount is: {discounted_price}")