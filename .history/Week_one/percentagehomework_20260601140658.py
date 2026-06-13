#percentage homework
#first homework .Collect the price of an item and the percentage discount, then subtract the discounted price .
price = float(input("Enter the price of the item: "))
#percentage discount
discount_percentage = float(input("Enter the percentage discount: "))
#calculate the discount amount
discount_amount = (discount_percentage / 100) * price
#calculate the discounted price
discounted_price = price - discount_amount
#output
print(f"The discounted price of the item is: {discounted_price}")