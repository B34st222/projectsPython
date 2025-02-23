from time import sleep

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

t1 = 25
t2 = 5

def timer(t):
    tmin = int(t)
    tsec = int(t * 60 % 60)

    
    while True:
        
        sleep(1)
        print(CLEAR)
        tsec -= 1

        if tsec == -1:
            tsec = 59
            tmin -= 1

        if tmin == -1:
            break

        print(f"{CLEAR_AND_RETURN}{tmin} : {tsec}")    
        



def main(t1, t2):
    
    while True:
        timer(t1)
        print("Cest le temps dune pause")
        pause=input("Q pour quitter, enter pour continuer")
        if ("q" or "Q") in pause:
            break


        timer(t2)
        print("Cest le temps de travailler")
        pause=input("Q pour quitter, enter pour continuer\n")
        if ("q" or "Q") in pause:
            break

main(t1, t2)
