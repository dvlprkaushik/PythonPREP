import random as rand

def game(comp, user):
    choice = "Yes"
    while (choice != "No"):
        if (comp == user):
            print("It's a tie!")
        elif ((comp == 'S' and user == 'W') or (comp == 'W' and user == 'G') or (comp == 'G' and user == 'S')):
            print('Computer Wins')
        else:
            print('User Wins')
        choice = input('Want to play again? "Yes" or "No": ')
        if choice != "No":
            user = input('Enter your choice (S, W, or G): ')
            comp = comChoice()

def comChoice():
    randomNum = rand.randint(0, 2)
    if (randomNum == 0):
       return 'S'
    elif (randomNum == 1):
       return 'W'
    elif (randomNum == 2):
       return 'G'


computer = comChoice()
User = input('Enter your choice : ')
game(computer, User)
