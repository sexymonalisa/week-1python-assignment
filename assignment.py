num1 = float(input("enter first number: ")) 
num2 = float(input("enter second number "))
op = input("enter operation (+, -, *, / ): ")

if op =="+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
   if num2 != 0:
       result = num1 / num2
else:
       print("Error: cannot divide by zero!" )
       exit()
print(f"{num1} {op} {num2} = {result}") 
