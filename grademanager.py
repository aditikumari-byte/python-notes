students = []

def add_student(name, grade):
    student = {"name": name, "grade": grade}
    students.append(student)

def show_all_students():
    print("\n--- All Students ---")
    for student in students:
     print(f"{student['name']}: {student['grade']}")

def calculate_average():
    if len(students) == 0:
        return "No students"

    total = 0
    for student in students:
        total += student['grade']

    average = total/len(students)
    return average

def find_highest():
    if len(students) == 0:
      print("No students")

    highest = students[0]
    for student in students:
        if student['grade'] > highest['grade']:
            highest = student
    return highest

def find_lowest():
    if len(students) == 0:
       print("No students")

    lowest = students[0]
    for student in students:
        if student['grade']< lowest['grade']:
            lowest = student
    return lowest 



while True:
   print("\n--- Grade Manager ---")
   print("1. Add student")
   print("2. Show all students")
   print("3. Show average")
   print("4. Show highest grade")
   print("5. Show lowest grade")
   print("6. Exit")

   choice = input("Choose one option(1-6): ") 

   if choice == "1":
        name = input("Student Name: ")
        grade = float(input("Student Grade: ")) 
        add_student(name, grade)
        print(f"Added {name} with grade {grade}.")

        add_more_information = input("Do you want to add more information(yes/no): ")
        if add_more_information.lower() != "yes":
         print('bye')
         break


   elif choice == "2":
     show_all_students()

   elif choice == "3":
      print(f'\nAverage grade: {calculate_average()}')

   elif choice == '4':
      highest = find_highest()
      if highest:
         print(f"\nHighest score:{highest['name']} with {highest['grade']}")

   elif choice == '5':
      lowest = find_lowest()
      if lowest:
         print(f"\nLowest score: {lowest['name']} with {lowest['grade']}")   

   elif choice == '6':
      print("Gooddbye")
      break
   
   else:
     print("Invalid entry") 

