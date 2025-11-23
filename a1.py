import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def player_move(board, symbol):
    move=-1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move=int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move-1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move-1]=symbol
#   - Purpose: Prompt the player for a move and update the board.
#   - Loop until a valid move is entered (number 1-9 and an available spot).
#   - Update the board at the chosen index with the player's symbol.

def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy=board.copy()
            board_copy[i]=ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i]=ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy=board.copy()
            board_copy[i]=player_symbol
            if check_win(board_copy, player_symbol):
                board[i]=ai_symbol
                return
    possible_moves=[i for i in range(9) if board[i].isdigit()]
    move=random.choice(possible_moves)
    board[move]=ai_symbol
 

#   - Purpose: Decide and execute the AI's move.
#   - For each free spot, simulate placing ai_symbol:
#         * If that move wins the game (using check_win), place the symbol and return.
#   - For each free spot, simulate placing player_symbol:
#         * If that move would let the player win, block it by placing ai_symbol and return.
#   - Otherwise, choose a random available move and place ai_symbol.

def check_win(board, symbol):
    win_conditions=[
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for cond in win_conditions:
        if board[cond[0]]== board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False
#   - Purpose: Check if the given symbol has met any winning condition.
#   - Define winning conditions (horizontal, vertical, diagonal).
#   - Return True if any condition is met; otherwise, return False.

def check_full(board):
    return all(not spot.isdigit()for spot in board)

#   - Purpose: Check if the board is completely filled.
#   - Return True if no cell contains a digit (i.e., all spots are taken).

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name=input(Fore.GREEN + "ENter your name: " + Style.RESET_ALL)
    while True:
        board=['1','2','3','4','5','6','7','8','9']
        player_symbol, ai_symbol=player_choice()
        turn="Player"
        game_on= True
        while game_on:
            display_board(board)
            if turn =='Player':
                player_move (board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print("Congratulations!"+ player_name +", you have won the game!")
                    game_on = False
                else:
                    if check_full (board):
                        display_board (board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print("AI has won the game!")
                    game_on = False
                else:
                    if check_full (board):
                        display_board (board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'Player'
        play_again=input("Do you want to play again? (yes/no): ").lower
        if play_again != 'yes':
            print("Thank you for playing!")
            break

#   - Purpose: Main game loop for Tic-Tac-Toe.
#   - Welcome the player and prompt for the player's name (display prompt in green).
#   - Loop to play games until the player chooses not to continue:
#         * Initialize the board with cell numbers.
#         * Get player's and AI's symbols via player_choice().
#         * Set the starting turn to 'Player'.
#         * While the game is on:
#               - Display the board.
#               - If it's the player's turn:
#                     > Call player_move() to get and execute the player's move.
#                     > Check if the player wins using check_win(); if so, display a win message and end the game.
#                     > Else, if the board is full, display a tie message and break.
#                     > Otherwise, set turn to 'AI'.
#               - If it's the AI's turn:
#                     > Call ai_move() to decide and execute the AI's move.
#                     > Check if the AI wins; if so, display a win message and end the game.
#                     > Else, if the board is full, display a tie message and break.
#                     > Otherwise, set turn to 'Player'.
#         * After the game ends, prompt the player if they want to play again.
#         * If the player does not type 'yes', exit the loop and thank the player.
#
# If the script is executed as the main module, call tic_tac_toe() to start the game.
if __name__ == "__main__":
    tic_tac_toe()



