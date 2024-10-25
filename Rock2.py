import random

def get_user_choice():
    """
    Prompt the user to enter their choice.
    Returns the choice if valid, else prompts again.
    """
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, scissors or quit to exit): ").lower()
        if user_input in choices:
            return user_input
        elif user_input == 'quit':
            return 'quit'
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """pp
    Randomly select the computer's choice.
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    """
    Determine the winner of the game.
    Returns a string indicating the result.
    """
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """
    Main function to play the game.
    """
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye.")
            break
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result + "\n")

if __name__ == "__main__":
    play_game()