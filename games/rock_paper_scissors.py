import random
class RockPaperScissors:
    def __init__(self):
        self.choices=["rock", "paper","scissors"]

    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def who_is_winner(self, player_choice, comp_choice):
        if player_choice== comp_choice:
            return "It's a tie!"
        elif (player_choice=="rock" and comp_choice=="scissors") or \
             (player_choice=="scissors" and comp_choice=="paper") or \
             (player_choice=="paper" and comp_choice=="rock"):
             return "You win!"
        else:
            return"Computer Wins!"

    def play(self):
        player_choice=input("Enter rock, paper or scissors: "). lower()
        if player_choice not in self.choices:
            print("Invalid choice! Please try again.")
            return self.play()
        

        comp_choice= self.get_computer_choice()
        print(f"Computer chose: {comp_choice}")

        result=self.who_is_winner(player_choice, comp_choice)
        print(result)