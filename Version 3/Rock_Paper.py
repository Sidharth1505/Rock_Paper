import random
from config import Choice,Files
from config import victory
from utils import Data
import json

class Rock:
    user_name = ''
    result = ''
    attempt = 0
    won = 0
    lose = 0
    
    def __init__(self,user_name):
        self.user_name = user_name


    def __user_selection(self):
        try:
            user_choice_prompt = int(input("\n\n Enter \n 1 for Rock.  \n 2 for Paper \n 3 for Scissors \n Please make your choice :: "))
            if user_choice_prompt not in [1,2,3]:
                print('Invalid Choice!!! Try Again\n')
                self.__user_selection()
            else:
                self.user_choice = Choice(user_choice_prompt)
        except ValueError:
            print('Enter numeric values only :')
            self.__user_selection()
    

    def __computer_selection(self):
        self.computer_choice = Choice(random.randint(1,3))


    def __determine_winner(self):
        self.attempt = self.attempt+1
        if self.user_choice == self.computer_choice:
           self.result = (f"Both players selected {self.user_choice.name.title()}. It's a tie!")
        elif self.computer_choice == victory[self.user_choice]:
            self.result = (f"{self.user_choice.name.title()} beats {self.computer_choice.name.title()} !! You Won \n")
            self.won+=1
        else:
            self.result = (f"{self.computer_choice.name.title()} beats {self.user_choice.name.title()} !! You Lose \n")
            self.lose+=1
    
    def __show_result(self):
        print('\n Here we go : \n {} Chose {} \n Computer chose {} \n The Result is \n {} \n'.format(self.user_name,self.user_choice.name.title(), self.computer_choice.name.title(), self.result))

    def show_score(self):
        file = Data.fetch_data(self)
        file[self.user_name]["Games_Played"][0]["Rock Paper Scissors"]["Attempts"]  =  self.attempt+ 10 
        file[self.user_name]["Games_Played"][0]["Rock Paper Scissors"]["Won"]  =  self.won +10
        Data.append_data(self,file)
        print('Scores ')
        print(f'Total No. of Game Played : {self.attempt}')
        print(f'{self.user_name} Won {self.won}')
        print(f'Computer won {self.lose}')


    def play(self):
        while True:
            self.__user_selection()
            self.__computer_selection()
            self.__determine_winner()
            self.__show_result()
            play_again = input('\n Do you want to play again ? \n Press Y for yes and N for No :::: ').lower()
            if play_again.isdigit() and play_again not in ['y', 'n']:
                print('Game Terminating due to invalid Choice')
            else:
                if play_again == 'y':
                    continue
                else:
                    break





