from User_Authentication import Authenticate
from Rock_Paper import Rock
from Number_Guessing import Number

class Game_Play:
    def play(self, user_name):
        while True:
            print('Enter 1 for Rock Paper and Scissors\nEnter 2 for Number Guessing\n ')
            choice = int(input('Enter your choice :'))
            try:
                if choice ==1:
                    rock = Rock(user_name)
                    rock.start_game()
                    rock.show_score()
                elif choice== 2:
                    number= Number()
                    number.play(user_name)
                else:
                    print('Enter Correct option! Try Again\n')
                    self.play()
            except:
                print('Enter Numeric Value Only \n\n')
                self.play()
            print('\nWant to Play Again\nPress Y for yes \nPress N for No')
            play_again_decision = input('Please Make a Choice : ')
            if play_again_decision in ['N','n']:
                print('\nThanks for Playing :-|) ')
                return
            else:
                self.play(user_name)

if __name__ == '__main__':
    user = Authenticate()
    name = user.choice()
    game = Game_Play()
    game.play(name)

