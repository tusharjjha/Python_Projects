temperature = float(input("Enter the temperature: "))
unit = input("Is the temperature in calsius(c) or fehrenheit(f): ")

if unit =="c":
    temperature = round(((9 * temperature)/ 5 + 32), 1)
    print(f"The temperature in fehenheit is: {temperature}F")
          

elif unit =="f":
    temperature = round(((temperature - 32) * 5 / 9), 1)
    print(f"The temperature in Celsius is: {temperature}C")

else:
    print(f"{unit} is an invalid unit of measurement")