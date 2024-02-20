import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user_choice == 'q':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        winner = get_winner(user_choice, computer_choice)
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    main()