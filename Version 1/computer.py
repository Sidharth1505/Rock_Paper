
import random

class ComputerGuess():
    def __init__(self,low,high,feedback,ct,guess):
        self.low=low
        self.high=high
        self.feedback=feedback
        self.ct=ct
        self.guess=guess
      
    def computer_chance(self):
        while self.feedback != 'c' :
            if self.low != self.high :
                self.guess = random.randint(self.low,self.high)
            else:
                self.guess=self.high
            
            self.feedback=input(f'Is {self.guess} too HIGH (H) , too LOW (L) or Correct (C)??  ').lower()
            if self.feedback == 'h':
                self.high = self.guess - 1
            elif self.feedback == 'l':
                self.low = self.guess + 1
            self.ct=self.ct+1
    
    def result(self):
        print(f'YaY! computer guessed the Number, {self.guess} , correctly in {self.ct} attempts!!')
        return self.ct
        
if __name__=="__main__":
    username=input("Enter User Name: ")
    n=int(input("Enter the range: "))
    comp=ComputerGuess(1,n,"",0,0)
    comp.computer_chance()
    attempts_score=comp.result()
    with open("result.txt","w") as file:
        file.write("Username: ")
        file.write(username)
        file.write("\nAttempts: ")
        file.write(str(attempts_score))
        file.write("\n")
        
    with open("result.txt","r") as file:
        print(file.read())