unit = str(input("Is this unit in Celsius, Fahrenheit or Kelvin? (C/F/K): ").strip().title())

if unit == "C":
    u = "Celsius Scale" 
    temp = float(input(f"Enter the temperature in {u}: "))
    tcu = str(input("Do you want to convert it to Fahrenheit or Kelvin? (F/K): ").strip().title())

    if tcu == "F":
        ftemp = (temp * 1.8) + 32
        print(f"{temp}°{unit} is {round(ftemp, 2)}°{tcu}.")
    elif tcu == "K":
        ftemp = (temp + 273.15)
        print(f"{temp}°{unit} is {round(ftemp, 2)}{tcu}.")
    else:
        print("The unit to be converted is invalid.")
    
elif unit == "F":
    u = "Fahrenheit Scale"
    temp = float(input(f"Enter the temperature in {u}: "))
    tcu = str(input("Do you want to convert it to Celsius or Kelvin? (C/K): ").strip().title())
    
    if tcu == "C":
        ftemp = (temp - 32) / 1.8
        print(f"{temp}°{unit} is {round(ftemp, 2)}°{tcu}.")
    elif tcu == "K":
        ftemp = (temp - 32) / 1.8 + 273.15
        print(f"{temp}°{unit} is {round(ftemp, 2)}{tcu}.")
    else:
        print("The unit to be converted is invalid.")

elif unit == "K":
    u = "Kelvin Scale"
    temp = float(input(f"Enter the temperature in {u}: "))
    tcu = str(input("Do you want to convert it to Celsius or Fahrenheit? (C/F): ").strip().title())

    if tcu == "C":
        ftemp = temp - 273.15
        print(f"{temp}{unit} is {round(ftemp, 2)}°{tcu}.")
    elif tcu == "F":
        ftemp = (temp - 273.15) * 1.8 + 32
        print(f"{temp}{unit} is {round(ftemp, 2)}°{tcu}.")
    else:
        print("The unit to be converted is invalid.")

else: 
    print("The unit given is invalid.")