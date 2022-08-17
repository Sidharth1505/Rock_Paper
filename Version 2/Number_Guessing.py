
import random
from user import UserChance
from computer import ComputerGuess

class Number:
    def play(self, user_name):
        while True:
            try:
                x=int(input("Press 1 for USER GUESS or Press 2 for COMPUTER GUESS: "))
                if x==1:
                    n=int(input("Enter Range you want to play: "))
                    number=random.randint(0,n)
                    user=UserChance(number,'')
                    user.play()
                    print()
                    #print("Score: ",user.result())
                    score_user=user.result()
                    with open("result.txt","a") as file:
                        s = (f'Username : {user_name}\n Game Played :  Number Guessing \n Score : {score_user}\n\n')
                        file.write(s)
                        # file.write("Username: ")
                        # file.write(user_name)
                        # file.write("\nScore: ")
                        # file.write(str(score_user))
                        # file.write("\n")
                        
                    # with open("result.txt","r") as file:
                    #     print(file.read())
                    print(s)
                elif x==2:
                    n=int(input("Enter the range: "))
                    comp=ComputerGuess(1,n,"",0,0)
                    comp.computer_chance()
                    attempts_score=comp.result()
                    with open("result.txt","a") as file:
                        s = (f'Username : {user_name}\n Game Played :  Number Guessing \n Attempts : {attempts_score}\n\n')
                        # file.write("Username: ")
                        # file.write(user_name)
                        # file.write("\nAttempts: ")
                        # file.write(str(attempts_score))
                        # file.write("\n")
                        file.write(s)
                        
                    # with open("result.txt","r") as file:
                    #     print(file.read())
                    print(s)
                else:
                    print("Please enter either 1 or 2 !!")
            
            except:
                print("Please give Intger Input only!!")
            else:
                c=input("Do you want to continue!! Press Yes(Y) or NO(N) ").lower()
                if c=='n':
                    break;
                else:
                    continue


# if __name__=="__main__":

#     print("-----------------------------------------------------------")
#     print("-------------- Code Successfully Executed !! --------------")
    
    