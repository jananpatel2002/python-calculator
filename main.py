import art 
from replit import clear
print(art.logo)

###  FUNCTIONS AND DATA ###
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-":subtract,
  "/":divide,
  "*":multiply
}

useAnswer = 'no'
### MAIN CODE ###
while(True):
  clear()
  if(useAnswer == 'yes'):
    n1 = answer
  else:
    n1 = int(input("What is your first number? "))
  
  for symbol in operations:
    print(symbol)
  
  symbol = input("Select any operation from above. ")
  while symbol not in operations:
    symbol = input("Please select a valid symbol from above: ")
  n2 = int(input("What is your second number? "))
  answer = operations[symbol](n1,n2) # Really simple code. Functions are stored above and then are accessed based on the input
  print(f"{n1} {symbol} {n2} = {answer}")
  
  useAnswer= input("Would you like to use this Answer for the next calculation? Yes or No: ").lower()


  