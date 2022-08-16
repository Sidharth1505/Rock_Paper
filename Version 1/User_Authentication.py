import bcrypt

class Authenticate:
    def register(self):
        db = open('user_data.txt', "r")
        user_name = input('Enter a user name: ')
        password = input('Enter a password : ')
        password1 = input('Please enter your password again : ')
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
                #password = password.encode('utf-8')
                #hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                #print(type(hashed))
                db = open('user_data.txt', 'a')
                db.write('{},  {}\n'.format(user_name, password))
                print('Success')
                print('Migrating to Game Play Window\n')
        return user_name

    def access(self):
        db  = open('user_data.txt', "r")
        UserName =  input('Enter the Username: ')
        Password = input('Enter the password: ')
        #Password = Password.encode('utf-8')
        if len(UserName or Password) >1:
            d = []
            f = []
            for i in db:
                a,b = i.split(',  ')             
                b = b.strip()
                #print(b)
                d.append(a)
                f.append(b)
            data  = dict(zip(d,f))
            #print(data)
            try: 
                if data[UserName]:
                    try:
                        #result = bcrypt.checkpw(Password, data[UserName])
                        if str(Password) == data[UserName]:
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
        choice =  int(input('Please Enter your Choice:  '))

        if choice ==1 :
            name = self.access()
        elif choice == 2:
            name = self.register()
        else:
            print('Enter a valid option')
            self.choice()
        return name




