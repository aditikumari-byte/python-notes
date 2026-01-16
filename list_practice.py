numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

numbers = [1,2,3,4,5]
squared = [{num**2} for num in numbers]
print(squared)

words = ['hello','world','python','coding']

uppercase_words = [word.upper() for word in words]
print(uppercase_words)

words = ['cat','elephant','dog','butterfly','ant']

long_words = [word for word in words if len(word)> 3]
print(long_words)

names = ['Alice','Bob','Charlie','Diana']
first_letters = [name[0] for name in names]
print(first_letters)

words = ['apple','pie','banana','kiwi','strawberry']
sorted_words = sorted(words, key =lambda x: len(x))
print(sorted_words)

numbers = [1,5,12,8,20,3,15]
filtered = list(filter(lambda x: x>10,numbers))
print(filtered)

prices = [10,20,30,40,50]
prices_with_tax = list(map(lambda x: x*1.1,prices))
print(prices_with_tax)

students= [
    ('Alice',85),
    ('Bob',92),
    ('Charlie', 78),
    ('Diana',95)
]
sorted_students = sorted(students, key=lambda x:x[1],reverse=True)
print(sorted_students)

words = ['apple','apricot','avocado']
a_words  = list(filter(lambda x: x[0]=='a',words))
print(a_words)