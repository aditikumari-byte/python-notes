students = []

def add_student(name,age,math,science,english):
    student = {"name" : name, "age" : age, "grades": {"Math" : math, "Science" : science, "English" : english}} 
    students.append(student)
    



def show_all_students():
    print("\n--- All students ---")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")
             
add_student('Priya',22,90,95,92)       
add_student('Aditi',25,80,90,70)  
add_student('Butter',20,90,60,80)



def calculate_averages():
    print("\n--- Averages ---")
    for student in students:
      total = sum(student['grades'].values())
      average = total/len(student["grades"])
      print(f"Name:{student['name']}, Average: {average:.2f}")

  

def find_top_students():
    averages = []
    for student in students:
      average =sum(student['grades'].values())/len(student['grades'])
      averages.append((student["name"],average))

    averages.sort(key=lambda x: x[1], reverse=True)

    print("\n--- Top Students ---")
    for name, average in averages[:3]:
      print(f"{name}:{average:.2f}")



def high_scores():
   print("\n--- Students with grades >80 ---")
   high_scores = []
   for student in students:
      average = sum(student['grades'].values())/len(student['grades'])
      if average > 80:
         high_score=average
         high_scores.append((student['name'],high_score))

   for name, score in high_scores:
      print(f"{name}:{score:.2f}")

     

def remove_student():
   name_to_remove = input("\nEnter student name to remove: ")
   for student in students:
      if student['name'] == name_to_remove:
       students.remove(student)
       print(f'Successfully removed {name_to_remove}')
       return students
   print("Student not found.")
   return students

 

while True:
   print("\n--- Student Management System ---")
   print("1. Add student")
   print('2. Show all students')
   print('3. Calculate average')
   print('4. Show top students')
   print('5. High Scores')
   print('6. Remove student')
   print('7. Exit')

   choice = input("\nChoose from 1-7: ")

   if choice == '1':
      name = input("Enter student name: ")
      age = int(input("Enter student age: "))
      math = float(input("Enter math grade: "))
      science = float(input("Enter science grade: "))
      english = float(input("Enter english grade: "))
      add_student(name, age, math, science, english)
      print(f"Added {name} successfully of Age: {age} with Grades: 'Math':{math}, 'English':{english}, 'Science':{science}")


   elif choice == '2':
     show_all_students()

   elif choice == '3':
     calculate_averages()

   elif choice == '4':
     find_top_students()

   elif choice == '5':
       high_scores() 

   elif choice == '6':
       remove_student() 

   elif choice == '7':
      print("Goodbye!")
      break

   else:
      print("Invalid entry!")          

