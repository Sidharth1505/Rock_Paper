from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER =2
    SCISSORS = 3

class Files(Enum):
    USER_DATA = 'user_data.json'

class Prompts(Enum):
    LOGIN_SUCCESS = 'Login Successful\n'
    INCORRECT = 'Incorrect Username or Password\n'
    USERNAME_DONT = "Username Doesn't Exist\n"
    SUCCESS = 'Success\n'
    MIGRATION = 'Migrating to Game Play Window\n'

victory = {
    Choice.ROCK : Choice.SCISSORS,
    Choice.PAPER : Choice.ROCK,
    Choice.SCISSORS : Choice.PAPER
    }
