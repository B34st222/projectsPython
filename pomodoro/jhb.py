import time


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

tempsPause = 1
tempsEtude = 1
tempsPauseSecondes = tempsPause * 60
tempsEtudeSecondes = tempsEtude * 60

def tempsEcoule(tempsVise):
    pomme = 0
    print(CLEAR)

    while pomme < tempsVise:
        time.sleep(1)
        pomme = pomme + 1

        tempsRestant = tempsVise - pomme
        minutesRestantes = tempsRestant // 60
        secondesRestantes = tempsRestant % 60


        print(f"{CLEAR_AND_RETURN}Temps restant: {minutesRestantes}:{secondesRestantes}")


def main(tempsWork, tempsBreak):
    while True:

        tempsEcoule(tempsWork)
        banane=input("C\'est le temps d\'une pause! ENTER pour continuer (q pour quitter)")
        if banane == "q":
            break

        tempsEcoule(tempsBreak)
        banane = input("C\'est le temps de travailler! ENTER pour continuer (q pour quitter)")
        if banane == "q":
            break


main(tempsEtudeSecondes,tempsPauseSecondes)
