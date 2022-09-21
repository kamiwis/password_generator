import random

def main():
  # Initialize lists with valid password characters.
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  # Greet user.
  print("Welcome to your password generator")
  # Prompt user for number of letters, numbers, symbols, and if first letter should be capitalized.
  num_letters = int(input("How many letters would you like your password to have?\n"))
  num_numbers = int(input("How many numbers would you like your password to have?\n"))
  num_symbols = int(input("How many symbols would you like your password to have?\n"))

  # Initialize password string. We will add to this as we pick random itesm from letters, numbers, and symbols.
  password = ""

  # Concatenate user-specified number of letters to the password string.
  for i in range(num_letters):
    password += random.choice(letters)
  
  # Concatenate user-specified number of symbols to the password string.
  for i in range(num_numbers):
    password += random.choice(numbers)
  
  # Concatenate user-specified number of numbers to the password string.
  for i in range(num_symbols):
    password += random.choice(symbols)
  
  print(password)








if __name__ == "__main__":
  main()