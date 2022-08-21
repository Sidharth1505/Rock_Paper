
import random

class UserChance():
    
    def __init__(self,num,msg,res=0):
        self.num = num
        self.msg=msg
        self.res=res
        
    def play(self):
        attempt = 4
        initial=attempt
        while attempt > 0:
            try:
                user_input = int(input('Enter Number: '))
                if user_input == self.num:
                    self.msg = '---------You Won!---------'
                    print(f'''
                    ---------------------------
                    Correct answer: {self.num}
                    ---------------------------
                    ''')
                    self.res=attempt
                    print("Number of turns you have used: ",initial-attempt+1)
                    break
                elif user_input > self.num:
                    print(f'{user_input} is greater.\nRemaining attempts: {attempt-1}.')
                    attempt -= 1
                    

                elif user_input < self.num:
                    print(f'{user_input} is smaller.\nRemaining attempts: {attempt-1}.')
                    attempt -= 1

                else:
                    print('Something went wrong!')
                    break
            except ValueError:
                print("Please Enter Integer only!!")
            
        else:
            print()
            print(f'''
            ---------------------------
            "!! OOPS Out of Attempt !!"
            ---------------------------
            ''')
            self.msg="---------You Lost--------"
            
    def result(self):
        print(self.msg)
        self.res=self.res*10
        return self.res

    
if __name__=="__main__":
    username=input("Enter User Name: ")
    n=int(input("Enter Range you want to play: "))
    number=random.randint(0,n)
    user=UserChance(number,'')
    user.play()
    print()
    #print("Score: ",user.result())
    score_user=user.result()
    with open("result.txt","w") as file:
        file.write("Username: ")
        file.write(username)
        file.write("\nScore: ")
        file.write(str(score_user))
        file.write("\n")
        
    with open("result.txt","r") as file:
        print(file.read())