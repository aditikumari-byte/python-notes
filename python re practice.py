class Book:

    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def is_long(self):
        return self.pages > 300


book = Book("Harry","JK",400)
print(book)
print(book.is_long())








class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount >0:
            self.balance += float(amount)
            return True
        return False

    def withdraw(self,amount):
        if amount >0 and self.balance >= float(amount):
            self.balance -= float(amount)
            return True
        return False

    def __str__(self):
        return f"BankAccount (owner ='{self.owner}', balance = {self.balance:.2f})"
    




class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = [] #List to store grades

    def add_grade(self,grade):
        """Add a grade to the student's record"""
        if isinstance( grade,(int,float)) and 0<= grade <= 100:
            self.grades.append(float(grade))
            return True
        return False

    def get_average(self):
        """Return the average of all grades. Return 0 if no grades.""" 
        if not self.grades:
            return 0.0
        return sum(self.grades)/ len(self.grades)

    def __str__(self):
        """Return a nice string representation of the student""" 
        avg = self.get_average()
        return f"Student(name = '{self.name}', grades = {self.grades}, average = {avg:.2f})"
    



# Create a student
student = Student("Aditi",0)

# Add grades
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.add_grade(95)

print(student)