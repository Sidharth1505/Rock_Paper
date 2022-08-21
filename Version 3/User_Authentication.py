import maskpass
import hashlib
from config import Files,Prompts
from utils import Data
import json


class Authenticate:
    def __register(self):
        file = Data.fetch_data(self)
        user_name = input('Enter a user name: ')
        password = maskpass.askpass(prompt = 'Enter a Password: ', mask = '*')
        password1 = maskpass.askpass(prompt = 'Please enter your password again : ', mask='*')
        if(password != password1):
            print("Password Don't Match")
            self.register()
        else:
            if len(password)<=6:
                print('Password too short, Try Again')
                self.register()

            elif user_name in file.keys():
                print('Username Already Exists !! \n Try Again')
                self.register()
            else:
                password = password.encode('utf-8')
                hashed = hashlib.sha256(password).hexdigest()

                new_data = {
                    "Password" : hashed,
                    "Games_Played": [
                                {
                                    "Rock Paper Scissors": {
                                    "Attempts": 0,
                                    "Won": 0
                                    }
                                },
                                {
                                    "Number Guessing": {
                                    "Score" :  0
                                    }
                                }
                                ]
                    }
            file[user_name] = new_data  

            Data.append_data(self,file)
            print(Prompts.SUCCESS.value)
            print(Prompts.MIGRATION.value)
            return user_name

    def __access(self):
        file = Data.fetch_data(self)
        UserName =  input('Enter the Username: ')
        Password = maskpass.askpass('Enter the Password : ')
        Password = Password.encode('utf-8')
        check_password = hashlib.sha256(Password).hexdigest()
        if len(UserName or Password) >1:
            try: 
                if file[UserName]:
                    try:
                        if str(check_password) == file[UserName]["Password"]:
                            print(Prompts.LOGIN_SUCCESS.value)
                            print(f'Hi {UserName.upper()}')
                            print('Migrating to Game Play Window\n')
                        else:
                            print(Prompts.INCORRECT.value)
                            self.choice()
                    except Exception:
                        print(Prompts.INCORRECT.value)
                        self.choice()
                else:
                    print(Prompts.USER_DONT.value)
                    self.choice()
            except KeyError:
                print(Prompts.USER_DONT.value)
                self.choice()
        else:
            print('Please Enter a value')
            self.choice()

        return UserName


    def choice(self):
        print('\nWelcome!')
        print('Enter 1 for Login \nEnter 2 for Signup \n')
        try:
            choice =  int(input('Please Enter your Choice:  '))
            if choice ==1 :
                name = self.__access()
            elif choice == 2:
                name = self.__register()
            else:
                print('Enter a valid option')
                self.choice()
        except ValueError:
            print('Enter numeric value only !!! Try Again')
            self.choice()
        return name
