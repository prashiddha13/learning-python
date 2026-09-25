import random

low = 1
high = 100

num = random.randint(low, high)
g = 0
n = 0
print(f"The range is from {low} to {high}")
while n != num:
    try:
        n = int(input("Guess the number, n: "))
        if n > high:
            print(f"Your guess exceeded {high}. n is within the range")
            n = high
        elif n < low:
            print(f"Your guess preceeded {low}. n is within the range")
            n = low
        else:
            if n > num:
                print()
                print("n is lower than that.")
                print()
                high = n
            elif n < num:
                print()
                print("n is higher than that.")
                print()
                low = n

        print(f"Help: Between {low} and {high}")
        g += 1

    except ValueError:
        print("Invalid input. Please enter a number.")
print()
print("-------------------------------------------------")
print(f"Correct! The number to be guessed (n) was {num}.")
print()
print(f"Guess count = {g}")
print("-------------------------------------------------")
