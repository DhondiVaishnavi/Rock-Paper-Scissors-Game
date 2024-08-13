import random

class Game:

    def __init__(self) -> None:
        self.options = ['rock','paper','scissor']
        self.computer_choice=random.choice(self.options)

    def RockPaperScissor(self, user_choice):
        if user_choice in self.options:
            print('Computer choice : ', self.computer_choice)
            if self.computer_choice == user_choice:
                print("Draw")
            elif (self.computer_choice == 'rock' and user_choice == 'scissor')or(self.computer_choice == 'paper' and user_choice == 'rock')or(self.computer_choice == 'scissor' and user_choice == 'paper'):
                print("You Lose") 
            else:
                
                print("You Win")
        else:
            print('\n Invalid option please select (rock, paper, scissor)')


if __name__ == '__main__':
    user_choice=input('Enter your choice (rock,paper,scissor) : ').lower()
    run = Game()
    run.RockPaperScissor(user_choice)