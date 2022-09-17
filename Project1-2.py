# Programmer Name : Ani Ohanian
# Date: 7/23/22
# Description: This Program calculates the discounted price of an item using the if-elif-else statement.
# Conditions are as follows:
# If the price is 300 or above, it will be discounted by 30%
# If the price falls between 200 and 300, it will be discounted by 20%
# If the price falls between 100 and 200, it will be discounted by 10%
# If the price is less than 100, it will be discounted by 5%
# There is no discount for negative prices.

price = float(input("Please enter the price of an item to give you the discounted price: $"))

if price >= 300:
    price -= ((30/100) * price)
    print("You are going to get a 30% discount. Your discounted price will be: $"+ format(price,'.2f'))

elif price >= 200:
    price -= ((20/100)* price)
    print("You are going to get a 20% discount. Your discounted price will be: $"+ format(price,'.2f'))

elif price >= 100:
    price -= ((10/100)* price)
    print("You are going to get a 10% discount. Your discounted price will be: $"+ format(price,'.2f'))
    
elif price > 0:
    price -= ((5/100) * price)
    print("You are going to get a 5% discount. Your discounted price will be: $"+ format(price,'.2f'))

else:
    # this is for zero or negative price
    print("There is no discount.")