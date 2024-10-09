import random


board = [0] * 100
board[0] = 37
board[3]=13
board[7]=29
board[20]=41
board[27]=75
board[31]=9
board[35]=5
board[47]=25
board[49]=66
board[61]=17
board[70]=91
board[79]=98
board[87]=23
board[94]=55
board[96]=77

def joueurs():
    nom=input("Nom du joueur: ")
    return nom

def dice():
    roll = random.randint(1,6)
    return roll





def main():
    j1 = joueurs()
    j2 = joueurs()



main()