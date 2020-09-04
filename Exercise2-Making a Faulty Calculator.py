n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
opt = input("Enter your operator {+ , - , * , / }: ")

if opt == "+":
if n1 == 56 and n2 == 9:
print("Your answer is 77.")
else:
print("Your answer is ", n1 + n2)
elif opt == "-":
print("Your answer is ", n1 - n2)
elif opt == "*":
if n1 == 45 and n2 == 3:
print("Your answer is 555.")
else:
print("Your answer is ", n1 * n2)
elif opt == "/":
if n1 == 56 and n2 == 6:
print("Your answer is 4")
else:
print("Your answer is ", n1 / n2)
