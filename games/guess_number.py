import random

class GuessNumber:
    def __init__(self, low=1, high=10):
        self.low = low
        self.high = high
        self.target = random.randint(self.low, self.high)
    
    def play(self):
        print(f"Guess a number between {self.low} and {self.high}!")
        n=1
        while n<=3:
            try:
                guess = int(input("Your guess: "))
                if guess < self.low or guess > self.high:
                    print(f"Please enter a number between {self.low} and {self.high}.")
                elif guess < self.target:
                    print("Too low! Try again.")
                elif guess > self.target:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You guessed it right!")
        
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            n+=1
        
       


