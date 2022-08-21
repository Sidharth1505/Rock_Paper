
import random
from user import UserChance
from computer import ComputerGuess
from config import Files
from utils import Data
import json
class Number:

    def __init__(self, user_name):
        self.user_name = user_name
    
    def play(self):
        while True:
            try:
                x=int(input("Press 1 for USER GUESS or Press 2 for COMPUTER GUESS: "))
                if x==1:
                    n=int(input("Enter Range you want to play: "))
                    number=random.randint(0,n)
                    user=UserChance(number,'')
                    user.play()
                    print()
                    score_user=user.result()
                    s = (f'Username : {self.user_name}\n Game Played :  Number Guessing \n Score : {score_user}\n\n')
                    file = Data.fetch_data(self)
                    file[self.user_name]["Games_Played"][1]["Number Guessing"]["Score"]  += score_user
                    Data.append_data(self,file)
                    print(s)
                elif x==2:
                    n=int(input("Enter the range: "))
                    comp=ComputerGuess(1,n,"",0,0)
                    comp.computer_chance()
                    attempts_score=comp.result()
                    s = (f'Username : {self.user_name}\n Game Played :  Number Guessing \n Score : {attempts_score}\n\n')
                    file = Data.fetch_data(self)
                    file[self.user_name]["Games_Played"][1]["Number Guessing"]["Score"] +=  attempts_score
                    Data.append_data(self,file)
                    print(s)
                else:
                    print("Please enter either 1 or 2 !!")
            
            except ValueError:
                print("Please give Intger Input only!!")
            else:
                c=input("Do you want to continue!! Press Yes(Y) or NO(N) ").lower()
                if c=='n':
                    break
                else:
                    continue


# if __name__=="__main__":

#     print("-----------------------------------------------------------")
#     print("-------------- Code Successfully Executed !! --------------")
    
    