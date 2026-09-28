import random
import string

characters = " " + string.ascii_letters + string.digits + string.punctuation #
characters = list(characters) #

enc = characters.copy() #
random.shuffle(enc) #
 
#To encrypt 
user_input = str(input("Enter your message to encrypt: "))
enc_output = "" #

for letter in user_input:
    place = characters.index(letter) #This assigns the index value of that letter to the variable place. 
    enc_output += enc[place] ###

print(enc_output)

#To decrypt
user_input = str(input("Enter your message to decrypt: "))
denc_output = ""

for letter in user_input:
    place = enc.index(letter) 
    denc_output += characters[place] 

print(denc_output)



