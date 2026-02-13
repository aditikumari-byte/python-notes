50 - 5*6
20
70 + 60/2 # division always returns a floating-point number
100.0
19//2 # removes the decimal 
9
19%2
1 #remainder of the division
5**2 #5 squared
25
s = 'First line. \nSecond line.'
s
'First line.\n Second line'
print (s)

#Example 1: With initaila newline
message1 = """
Hello
World
"""
print ("Example 1:")
print (message1)
message2 = """\
Hello
World
"""
print ("Example 2:")
print (message2)
word = 'Python'
new_word ='J' + word[1:]
print(new_word)
word[:2] + 'py'
'Pypy'
s= 'asdfghjklqwertyuiop'
len(s)
19 # Length of the string
#Fibonacci serie:
#the sum of two elements defines the next
a,b = 0,1
while a < 10:
    print (a)
    a,b = b, a+b

def fib(n):
    """Print a Fibonacci series up to n."""
    a,b = 0,1
    while a<n:
        print(a, end=' ')
        a,b = b, a+b
    print()
fib(2000)  

def fib(n):
    """Print a Fibonacci series up to n."""
    x,y = 1,2
    while x<n:
        print(x, end=' ')
        x,y = y, x+y
    print()
fib(2000)

def f(a, L=None):
    if L is None:
        L= []
    L.append(a)
    return L
print(f(1))

#dangerouscase
def f(a,L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2)) # creates new list everytime with repeatation

def greet(name, msg="Hello"):
    print(msg,name)
greet("aditi")
greet("aditi","hi")

#Keyword arguments
def animal(name,type="cat"):
    print(name,type)
animal("meow")
animal("luck",type="dog")

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def is_adult(self):
        if self.age>= 18:
            print(f"{self.name} is an adult of age {self.age}.")
        else:
            print(f"{self.name} is not an adult.")    


class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount,'description': description})
        
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": - amount,"description": description})
            return True
        else:
            return False    


    def get_balance(self):
        balance=0
        for i in self.ledger:
            balance = balance + i["amount"]
        return balance  

    def transfer(self,amount,destination):
        if self.check_funds(amount):
            self.withdraw(amount, description = f"Transfer to {destination.name}")
            destination.deposit(amount, description= f"Transfer from {self.name}")
            return True
        else:
            return False    

    def check_funds(self,amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30,"*")
        output = title + "\n"
        
        for item in self.ledger:
            des= item["description"][:23].ljust(23)
            amt= f"{item['amount']:.2f}".rjust(7)
            output += des + amt + "\n"
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    
    category_spending = []
    
    for item in categories:
        spending=0
        
        for entry in item.ledger:
           if entry["amount"]< 0:
                spending += abs(entry["amount"])
        
        category_spending.append(spending)        
   
   # return category_spending

    total_spending = sum(category_spending)
    percentage = []

    for amount in category_spending:
        percent = (int((amount/total_spending)*100) // 10) *10
        percentage.append(percent)

    #return percentage   
    chart = "Percentage spent by category\n"
    for i in range(100,-1,-10):
        chart += f"{i:>3}| "
        for percent in percentage:
            if percent >= i :
                chart += "o  " 
            else:
                chart += "   "

        chart += "\n" 

    chart += "    " + ("-"* (len(categories)*3+1)) + "\n"     
    names=[category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "    
        if i < max_length -1:
            chart += "\n"    

    return chart        



from abc import ABC, abstractmethod

class Animal(ABC): # Inherits from abstract base class
   @abstractmethod # Abstract method decorator
   def make_sound(self):  # The method subclasses must override
       pass

# Concrete class that will override the abstract method
class Dog(Animal):
   def make_sound(self):
       print('Woof!')

# Another concrete class that will override the abstract method
class Cat(Animal):
   def make_sound(self):
       print('Meow!')

# Another concrete class that will override the abstract method
class Monkey(Animal):
   def make_sound(self):
       print('Ooh ooh aah aah!')

# Create instances of each concrete class
animals = [Dog(), Cat(), Monkey()]

# Loop through the instances to call the make_sound method
for animal in animals:
   animal.make_sound()

# Output:
# Woof!
# Meow!
# Ooh ooh aah aah!



from abc import ABC, abstractmethod

# The blueprint for any toy that can speak
class TalkingToy(ABC):
   def __init__(self, name):
       self.name = name
   @abstractmethod
   def speak(self):
       pass

class RobotToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
   def speak(self):
       print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says ROOOOAR!')

# Create toys
rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

toys = [rusty, fluffy, rex]
for toy in toys:
   toy.speak()

# Output:
# Rusty says beep boop! I am a robot!
# Fluffy says hug me! I'm cuddly!
# Rex says ROOOOAR!


