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
  shuffle = input("Do you want your password shuffled? 'Y' or 'N'\n")

  # Initialize password list. We will add to this as we pick random items from letters, numbers, and symbols.
  password = []

  # Concatenate user-specified number of letters to the password string.
  for i in range(num_letters):
    password.append(random.choice(letters))
  
  # Concatenate user-specified number of symbols to the password string.
  for i in range(num_symbols):
    password.append(random.choice(symbols))
  
  # Concatenate user-specified number of numbers to the password string.
  for i in range(num_numbers):
    password.append(random.choice(numbers))

  # If user wants a shuffled password, convert password to list, shuffle, and convert back to a string.
  if shuffle == 'Y':
    random.shuffle(password)
  
  print("".join(password))

if __name__ == "__main__":
  main()