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

