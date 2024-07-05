1#making a simple python caclulator


#function of addition
def add(n1, n2):
  return n1 + n2


#function of subtraction
def sub(n1, n2):
  return n1 - n2


#function of multiplication
def mul(n1, n2):
  return n1 * n2


#function of division
def division(n1, n2):
  return n1 / n2


print("please select an operator-/n"
      " 1.add/n"
      "2.subtract/n"
      "3.multiply/n"
      "4.divide/n")

#taking input from user

select = int(input("select an operator 1,2,3,4:"))

number_1 = int(input("enter the first number"))
number_2 = int(input("enter the second number"))

if select == 1:
  print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
  print(number_1, "-", number_2, "=", sub(number_1, number_2))

elif select == 3:
  print(number_1, "*", number_2, "=", mul(number_1, number_2))

elif select == 4:
  print(number_1, "/", number_2, "=", division(number_1, number_2))
else:
  print("Invalid input")
