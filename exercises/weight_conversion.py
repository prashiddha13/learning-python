weight = float(input("Enter your weight: "))

print("Enter K if the unit is in Kgs")
print("Enter L if the unit is in Lbs")

i = str(input().title().strip())

if i == "K":
    cweight = weight * 2.20462
    print(f"{round(weight, 2)} kgs is equalt to {round(cweight, 2)} lbs")
elif i == "L":
    cweight = weight * 0.453592
    print(f"{round(weight, 2)} lbs is equalt to {round(cweight, 2)} kgs")
else: 
    print("Invalid input of unit")

