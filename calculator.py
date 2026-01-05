def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Cannot divide by zero"

def square(a,b):
    return a**b    

def remainder(a,b):
    return a%b

while True:

   print("Simple Calculator")
   print("1. Add")
   print("2. Subtract")
   print("3. Multiply")
   print("4. Divide")
   print("5. Square")
   print("6. Remainder")

   choice = input("Choose one function(1/2/3/4/5/6): ")

   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))

   if choice == "1":
    result = add(num1,num2)
    print(f"Result:{num1}+{num2}={result}")

   elif choice == "2":
     result = subtract(num1,num2)
     print(f"Result:{num1}-{num2}={result}")

   elif choice == "3":
     result = multiply(num1,num2)
     print(f"Result:{num1}*{num2}={result}")

   elif choice == '4':
     result = divide(num1,num2)
     print(f"Result:{num1}/{num2}={result}")

   elif choice == "5":
     result = square(num1,num2)
     print(f"Result:{num1}**{num2}={result}")

   elif choice =="6":
     result = remainder(num1,num2)
     print(f"Result:{num1}%{num2}={result}")

   else:
     print("Invalid entry!")

   calculate_again = input("Do you want to calculate again(yes/no): ")
   
   if calculate_again.lower() != "yes":
     print("Goodbye!")
     break