#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

================================================
password = []
for let in range(1, nr_letters+1):
    random_let = random.choice(letters)
    password.append(random_let)
for num in range(1, nr_numbers+1):
    random_num = random.choice(numbers)
    password.append(random_num)
for sym in range(1, nr_symbols+1):
    random_sym = random.choice(symbols)
    password.append(random.choice(symbols))
print( "".join(password)))

# ====================================================

easy_password = []
for let in range(1, nr_letters+1):
    easy_password.append(random.choice(letters))
for sym in range(1, nr_symbols+1):
    easy_password.append(random.choice(symbols))
for numb in range(1, nr_numbers+1):
    easy_password.append(random.choice(numbers))

print("Easy Level Password:", "".join(easy_password))

# =====================================================
# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = easy_password.copy()
random.shuffle(hard_password)

print("Hard Level Password:", "".join(hard_password))
