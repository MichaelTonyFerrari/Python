shirts = int(input("Enter how many shirts you want: "))

twelve = 12
seven = 7
three = 3

def discounts_Of_Shirts(shirts):

    price = 0

    if shirts >= 12:
        price = shirts*.40*14.95
    elif shirts >= seven and shirts < twelve:
        price = shirts*.30*14.95
    elif shirts >= three and shirts < seven:
        price = shirts*.20*14.95

    return price

def shipping_Of_Shirts(shirts):

    ship = 0
    shippingcost = 1.25
    ship = shirts*shippingcost
    return ship

if shirts >= 0 and shirts < three:
    tShirts = shirts*14.95
    shirtsShipping = shirts*1.25
    tot = tShirts + shirtsShipping
    print("Cost of T-shirts: ${}, Cost of Shipping: ${}, Total Cost: ${}".format(tShirts, shirtsShipping, tot))
else:

    orginialCost = 14.95*shirts
    discountCost = discounts_Of_Shirts(shirts)
    shippingPrice = shipping_Of_Shirts(shirts)

    costAfterDiscount = orginialCost - discountCost

    totalCost = costAfterDiscount + shippingPrice

    print("Cost of T-shirts: ${}, Cost of Shipping: ${}, Total Cost: ${}".format(costAfterDiscount, shippingPrice, totalCost))