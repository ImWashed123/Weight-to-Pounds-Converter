weight=eval(input("What is your weight? "))
unit=input("(K)g or (L)bs:" )
if unit.upper()=="K":
    convert=weight * 2.2
    print("Weight in lbs: " + str(convert))
else:
    convert=weight/2.2
    print("Weight in Kg: " + str(convert))