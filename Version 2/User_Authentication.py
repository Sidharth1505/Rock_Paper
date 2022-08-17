import maskpass
import hashlib

class Authenticate:
    def __register(self):
        db = open('user_data.txt', "r")
        user_name = input('Enter a user name: ')
        password = maskpass.askpass(prompt = 'Enter a Password: ', mask = '*')
        password1 = maskpass.askpass(prompt = 'Please enter your password again : ', mask='*')
        d = []
        f = []
        for i in db:
            a,b = i.split(',')
            b = b.strip()
            d.append(a)
            f.append(a)
        if(password != password1):
            print("Password Don't Match")
            register()
        else:
            if len(password)<=6:
                print('Password too short, Try Again')
                self.register()

            elif user_name in d:
                print('Username Already Exists !! \n Try Again')
                register()
            else:
                password = password.encode('utf-8')
                #hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                #print(type(hashed))
                hashed = hashlib.sha256(password).hexdigest()
                db = open('user_data.txt', 'a')
                db.write('{},  {}\n'.format(user_name, hashed))
                print('Success')
                print('Migrating to Game Play Window\n')
        return user_name

    def __access(self):
        db  = open('user_data.txt', "r")
        UserName =  input('Enter the Username: ')
        Password = maskpass.askpass('Enter the Password : ')
        Password = Password.encode('utf-8')
        #check_hashed = bcrypt.hashpw(Password, bcrypt.gensalt())
        check_password = hashlib.sha256(Password).hexdigest()
        if len(UserName or Password) >1:
            d = []
            f = []
            for i in db:
                a,b = i.split(',  ')             
                b = b.strip()
                d.append(a)
                f.append(b)
            data  = dict(zip(d,f))
            try: 
                if data[UserName]:
                    try:
                        #result = bcrypt.checkpw(Password, data[UserName])
                        if str(check_password) == data[UserName]:
                            print('Login Success!\n')
                            print(f'Hi {UserName.upper()}')
                            print('Migrating to Game Play Window\n')
                        else:
                            print('Incorrect Password or Username')
                            self.choice()
                    except:
                        print('Incorrect Password or Username')
                        self.choice()
                else:
                    print("Username doesn't exist")
                    self.choice()
            except:
                print("Username or Password doesn't exist")
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
        except:
            print('Enter numeric value only !!! Try Again')
            self.choice()
        return name




