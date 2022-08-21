import json
from utils import Data
from collections import OrderedDict
class LeaderBoard():

    def snake_leaderboard(self, file):
        data = {}
        for user in file.keys():
            data[user] = file[user]["Games_Played"][0]["Rock Paper Scissors"]["Won"]

        dictionary_keys = list(data.keys())
        sorted_dict = {dictionary_keys[i]: sorted(data.values(), reverse =True)[i] for i in range(len(dictionary_keys))}
        count = 1
        for key,value in sorted_dict.items():
            print(f"\t\t{count}\t\t{key}\t\t\t{value}\n")
            count+=1

        return sorted_dict


    def number_leaderboard(self,file):
        data = {}
        for user in file.keys():
            data[user] = file[user]["Games_Played"][1]["Number Guessing"]["Score"]

        dictionary_keys = list(data.keys())
        sorted_dict = {dictionary_keys[i]: sorted(data.values(), reverse = True)[i] for i in range(len(dictionary_keys))}
        count = 1
        for key,value in sorted_dict.items():
            print(f"\t\t{count}\t\t{key}\t\t\t{value}\n")
            count+=1

    def display(self):
        file  = Data.fetch_data(self)
        print('=================================================================\n')
        print('\t\t\tLEADERBAORD\t\t\t\t \n')
        print('=================================================================\n')
        print('\t\t\tROCK PAPER SCISSORS\t\t\t\t \n')
        print('-----------------------------------------------------------------\n')
        print("\t\tS.no\t\tName\t\tScore\n\n")
        self.snake_leaderboard(file)
        print('-----------------------------------------------------------------\n')
        print('\t\t\tNUMBER GUESSING\t\t\t\t \n')
        print('-----------------------------------------------------------------\n')
        print("\t\tS.no\t\tName\t\tScore\n\n")
        self.number_leaderboard(file)
        print('-----------------------------------------------------------------\n')


