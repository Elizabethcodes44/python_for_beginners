#online shopping checker: A user can only check out if they have items in their cart and have a valid payment method.else print "Cannot check out" with reasons

#variables
has_items_in_cart = True
has_valid_payment_method = False

#cond
if has_items_in_cart and has_valid_payment_method:
    print("You can check out")
else: print("Cannot check out because you either have no items in cart or you do not have a valid payment method")