#Python weight converter

weight = float(input("Enter your weight:"))
unit = input("killograms(k) or pounds(p)? ")
if unit == "k":
    weight = weight * 2.205
    unit = "lbs."
    print(f"Your Weight is: {round(weight, 2)} {unit}")

elif unit == "p":
    weight = weight / 2.205
    unit = "kg."
    print(f"Your Weight is: {round(weight, 2)} {unit}")

else:
    print(f"{unit} was not valid")
