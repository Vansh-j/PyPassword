#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
error = 0
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#exception handeling
try:
  nr_letters = int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  
except ValueError:
  print("Enter a valid input!")
  error = 1


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
if not error:

  password = ""
  for i in range(nr_letters):
    random_letters = random.choice(letters)
    password += random_letters


  for i in range(nr_symbols):
    random_symbols = random.choice(symbols)
    password+=random_symbols


  for i in range(nr_numbers):
    random_numbers = random.choice(numbers)
    password+=random_numbers


  password=list(password)

  random_password =[]

  for i in range(len(password)):
    x=random.choice(password)
    random_password.append(x)
    password.remove(x)

  random_password2=""
  for i in random_password:
    random_password2+=i


  print(random_password2)




