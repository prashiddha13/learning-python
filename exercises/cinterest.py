P = 0
rate = 0 
time = 0 

while P <= 0:
    P = float(input("What amount do you want to deposit?: "))
    if P <= 0: 
        print("The amount cannot be equal to or less than 0.")
    
while rate <= 0:
    rate = float(input("Enter the rate (in %) of interest: "))
    if rate <=0:
        print("The interest rate cannot be equal to or less than 0.")

while time <= 0:
    time = int(input("Enter the time (in years) that you want to deposit the amount: "))
    if time <= 0:
        print("The time cannot be equal to or less than 0.")

CI = P * ((1 + rate/100) ** time) 

# Hya tala ',' le european style ma comma haldinxa in the amount. And '.2f' le chai decimal lai 2 digits samma round garxa. same work as round function. 
print(f"The compound interest after {time} years is NPR {CI:,.2f}")
