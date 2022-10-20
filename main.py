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

def calculator():
  shouldContinue = True

  n1 = float(input("What is your first number? "))

  while(shouldContinue):
    
    for symbol in operations:
      print(symbol)
    
    symbol = input("Select any operation from above. ")
    while symbol not in operations:
      symbol = input("Please select a valid symbol from above: ")
    n2 = float(input("What is your second number? "))
    answer = operations[symbol](n1,n2) # Really simple code. Functions are stored above and then are accessed based on the input
    print(f"{n1} {symbol} {n2} = {answer}")
    
    if (input(f"Use {answer} in next calculation? Yes or No: ").lower() =='yes'):
      n1 = answer
    else:
      shouldContinue = False
      clear()
      calculator()

useAnswer = 'no'

### MAIN CODE ###


calculator()


  