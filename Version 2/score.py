
from user import UserChance

username=input("Enter User Name: ")
score_user=UserChance(1,"").result()
with open("result.txt","w") as file:
    file.write("Username: ")
    file.write(username)
    file.write("\nScore: ")
    file.write(str(score_user))
    
with open("result.txt","r") as file:
    print(file.read())
