import random

def display_choices(player_choice, ai_choice): 
    print("Your choice: ", end="")
    if player_choice == 'R':
        print("\nRock\n")  # Red
    elif player_choice == 'P':
        print("\nPaper\n")  # Blue
    else:
        print("\nScissors\n")  # Yellow
    
    print("AI choice:   ", end="")
    if ai_choice == 'R':
        print("\nRock\n")
    elif ai_choice == 'P':
        print("\nPaper\n")
    else:
        print("\nScissors\n")

def get_player_choice():
    choices = ['R', 'P', 'S']
    while True:
        choice = input("\nChoose Rock(R), Paper(P), or Scissors(S): ").upper()
        if choice in choices:
            return choice
        print("Invalid choice. Please enter R, P, or S.")
def ai_choice():
    return random.choice(['R', 'P', 'S'])
def determine_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "Tie"
    elif (player_choice == 'R' and ai_choice == 'S') or \
         (player_choice == 'P' and ai_choice == 'R') or \
         (player_choice == 'S' and ai_choice == 'P'):
        return "Player"
    else:
        return "AI"

def rock_paper_scissors():
    print("\nWelcome to Rock Paper Scissors!\n")
    player_name = input("\nEnter your name: ")
    
    while True:
        player_choice = get_player_choice()
        ai_choice_for_display = ai_choice()
        
        display_choices(player_choice, ai_choice_for_display)
        winner = determine_winner(player_choice, ai_choice_for_display)
        
        if winner == "Player":
            print(f"\nCongratulations {player_name}! You win!\n")
        elif winner == "AI":
            print("\nAI wins!\n")
        else:
            print("\nIt's a tie!\n")
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThank you for playing!\n")
            break
        else:
            rock_paper_scissors()
        print()

if __name__ == "__main__":
    rock_paper_scissors()
