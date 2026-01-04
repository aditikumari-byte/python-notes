import random
secret_number = random.randint(1, 100)
guesses = 0
print("I'm thinking of a number between 1 and 100!")
while True:
    try:
     user_guess = int( input("take a guess: "))
     guesses += 1
    except ValueError:
           print("Please enter a whole number between 1 and 100.")
    if user_guess == secret_number:
              print (f"Your guess is correct. The secret number is {secret_number}.")
              print (f"You took {guesses} guesses.")
              break
    elif user_guess < secret_number:
             print ("Your guess is too low.")
    else:
             print("Your guess is too high.")
    play_again = input("Play again? (yes/no): ")
    if play_again.lower()!= "yes":
     print("Thanks for playing!")
     break