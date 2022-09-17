numofguests = input ("How many people in your party? ")

intnumguests = int(numofguests)

for i in range(intnumguests):

    name = input("What is your name? ")
    lunch = input ("How much is your lunch item? ")
    drink = input("How much is your drink item? ")
    
    total = float(lunch) + float(drink)
    tip = total * .15
    checktotal = total + tip
    
    print (name)
    
    print(checktotal)