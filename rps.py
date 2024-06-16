import random

def get_user_choice():
    # Get the user's choice and ensure it is valid
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def get_computer_choice():
    # Randomly choose rock, paper, or scissors for the computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the choices
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    # Display the choices and the result
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0
    play_again = "yes"
    
    while play_again.lower() in ['yes', 'y']:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"Score: You {user_score} - {computer_score} Computer")
        play_again = input("Do you want to play again? (yes/no): ")
    
    print("Thank you for playing! Final Score:")
    print(f"You: {user_score} - Computer: {computer_score}")

if __name__ == "__main__":
    main()
