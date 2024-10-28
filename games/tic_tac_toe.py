class TicTacToe:
    def __init__(self):
        # Initialize the board with numbers representing available positions
        self.board = [str(i) for i in range(9)]
        self.current_winner = None
    
    def print_board(self):
        # Print the board in a simple 3x3 grid
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, position, player):
        # Place the player's mark on the chosen position if it's available
        if self.board[position] not in ['X', 'O']:
            self.board[position] = player
            return True
        return False

    def check_winner(self, player):
        # Check all winning combinations (rows, columns, diagonals)
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                self.current_winner = player
                return True
        return False

    def is_board_full(self):
        # Check if all positions are taken
        return all(spot in ['X', 'O'] for spot in self.board)

    def play(self):
        # Main game loop
        player = 'X'  # X always starts
        self.print_board()

        while not self.is_board_full():
            try:
                move = int(input(f"Player {player}, enter your move (0-8): "))
                if move not in range(9):
                    print("Invalid input. Please enter a number between 0 and 8.")
                    continue

                if self.make_move(move, player):
                    self.print_board()

                    if self.check_winner(player):
                        print(f"Player {player} wins!")
                        return

                    # Switch player
                    player = 'O' if player == 'X' else 'X'
                else:
                    print("That spot is already taken. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        print("It's a tie!")

