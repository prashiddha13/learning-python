# Menu ko items lai chai keys vando raixa and paxadi ko associated value lai chai value nai vando raich which does not necessiraly have to be a value in literal form, but can also be a string and other things. 
#First we build the menu using dictionary. 
menu = { "Popcorn-S" : 349, 
"Popcorn-M" : 449,
"Popcorn-L" :549, 
"Cheese Burger" : 299,
"Cold Drinks (250 ml.)" : 79,
"Extra Cheese" : 49, 
"Pizza-M" : 799,
"Combo set" : 1399
}
#Then we add the lists that we might require later. 
cart = []
total = 0
 
inum = 0
inums = []

#Now we print the menu. 
print("-----------------MENU-----------------")

for item, price in menu.items(): # .items() can be used to pick out whatever we want from the dict. 
    print(f"{inum + 1}. {item:21} : Rs. {price:,}/-")
    inum += 1
    inums.append(inum)

print("--------------------------------------")

#Now we ask the user for the input regarding what they want to buy and how much. 
while True:
    print("Enter '0' to quit. ")
    cartnum = int(input('Enter the S.No. of the item in the menu that you want to add to "YOUR CART". (for example: 1, 3, 8): '))
    

    if cartnum == 0: 
        break #means quit. 
    
    if cartnum in inums: 

        item, price = list(menu.items())[cartnum - 1] # .items() can be used to pick out whatever we want from the dict. here item is the first element and price is the second element of the index [cartnum -1].
        quant = int(input(f"How many {item}(s) would you like to buy?: "))
        cart.append((item, price, quant)) #I guess this is like appending tuple within a tuple. not so sure. 
    else: 
        print("The input is invalid. Try again. ")

#Now the cart printing and the calculation of the total. 
print()
print()
print()
print("----------------------------YOUR CART---------------------------")
for item, price, quant in cart:
    subtotal = price * quant 
    total += subtotal
    print(f"{item:25} Rs. {price:>5,} x {quant:^8} = Rs. {subtotal:>8,}/-")
print("----------------------------------------------------------------")
print(f"{'':41}Total = Rs. {total:>8,}/-")

