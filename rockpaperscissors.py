import random

def get_computer_choice():
    choices = ["rock","paper","scissor"]
    return random.choice(choices)

def determine_winner(player,computer):
    if player == computer:
      return "Tie"
    elif player == "rock" and computer == "scissor" or player=="scissor" and computer == "paper" or player == "paper" and computer == "rock":
       return "Win"
    elif player == "paper" and computer == "scissor" or player =="scissor" and computer=="rock" or player=="rock" and computer == "paper":
       return "Lose" 
    else:
       print("Invalid input")

def play_round():
   print("\nChoose:rock, paper, or scissor")
   player = input("Your choice: ").lower()

   computer = get_computer_choice()  
   print(f"Computer choice: {computer}")

   result = determine_winner(player,computer)

   if result == "Win":
      print("You win this round!")
      return "player"
   elif result == "Lose":
      print("Computer wins this round!")
      return "computer"
   else:
      print("It's a tie!")  
      return "Tie"   
    
player_score = 0
computer_score = 0

while True:
   print("\n--- Rock Paper Scissor ---")
   print(f"Score - You: {player_score} | Computer: {computer_score}")
   
   result = play_round()

   if result == "player":
      player_score += 1
   elif result == "computer":
      computer_score += 1    

   play_again = input("\nPlay again? (yes/no): ")
   if play_again.lower() != "yes":
        print(f"\nFinal Score - You: {player_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break
    
    