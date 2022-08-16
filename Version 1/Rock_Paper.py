import random

class Rock:
    possible_choices = ['rock','paper','scissors']
    user_choice=''
    computer_choice = ''
    user_name = ''
    result = ''
    attempt = 0
    won = 0
    lose = 0
    
    def __init__(self,user_name):
        self.user_name = user_name


    def __user_selection(self):
        user_choice_prompt = int(input("\n\n Enter \n 1 for Rock.  \n 2 for Paper \n 3 for Scissors \n Please make your choice :: "))
        if user_choice_prompt not in [1,2,3]:
            print('Invalid Choice!!! Try Again\n')
            self.__user_selection()
        else:
            self.user_choice = self.possible_choices[user_choice_prompt-1]
    
    def __computer_selection(self):
        self.computer_choice = random.choice(self.possible_choices)


    def __get_result(self):
        self.attempt = self.attempt+1
        if self.user_choice == 'rock':
            if self.computer_choice == 'rock':
                self.result = (f"Both players selected {self.user_choice}. It's a tie!")
            elif self.computer_choice == 'scissors':
                self.result = 'Rock smased Scissors !!!! You Won '
                self.won = self.won+1
            else:
                self.result = 'Paper covers rock! You lose.'
                self.lose = self.lose+1
        elif self.user_choice == 'paper':
            if self.computer_choice == 'paper':
                self.result = (f"Both players selected {self.user_choice}. It's a tie!")
            elif self.computer_choice == 'rock':
                self.result = 'Paper covers rock !!! You Won.'
                self.won = self.won+1
            else:
                self.result = 'Scissors cuts Paper ! You Lose'
                self.lose = self.lose+1
        else:
            if self.computer_choice == 'scissors':
                self.result = (f"Both players selected {self.user_choice}. It's a tie!")
            elif self.computer_choice == 'paper':
                self.result = 'Scissors cuts Paper ! You Won'
                self.won = self.won+1
            else:
                self.result = 'Rock smased Scissors !!!! You Lose'
                self.lose = self.lose+1

    def __show_result(self):
        print('\n Here we go : \n {} Chose {} \n Computer chose {} \n The Result is \n {} \n'.format(self.user_name,self.user_choice, self.computer_choice, self.result))
    def show_score(self):
        file = open('result.txt', "a")
        print('Scores ')
        print(f'Total No. of Game Played : {self.attempt}')
        print(f'{self.user_name} Won {self.won}')
        print(f'Computer won {self.lose}')
        file.write(f'UserName = {self.user_name} \nGame Played : Rock Paper Sccssiors \nScores \nTotal No. of Game Played : {self.attempt}\n{self.user_name} Won {self.won}\nComputer won {self.lose}\n Thank you for playing Rock Paper Scissors \n\n\n')

    def start_game(self):
        while True:
            self.__user_selection()
            self.__computer_selection()
            self.__get_result()
            self.__show_result()
            self.play_again = input('\n Do you want to play again ? \n Press Y for yes and N for No :::: ')
            if self.play_again in ['N','n']:
                break;
            else:
                self.start_game()






#if __name__ == "__main__":

   # player = Rock('Sid')
    # player.start_game()



