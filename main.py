from games.guess_number import GuessNumber
from games.rock_paper_scissors import RockPaperScissors
from games.tic_tac_toe import TicTacToe

def main():
    print("Welcome to Simple Game Collection")
    print("1. Guess the Number ")
    print("2. Rock Paper Scissors")
    print("3. Tic Tac Toe")
    choice=input("Enter a number to select game(1-3): ")

    if choice=="1":
        game=GuessNumber()
    elif choice=="2":
        game=RockPaperScissors()
    elif choice=="3":
        game=TicTacToe()
    else:
        print("Invalid choice. ")
        return
    
    game.play()

if __name__=="__main__":
    main()