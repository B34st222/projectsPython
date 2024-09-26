import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

minWork = 25
minOff = 5

secondWork = minWork * 60
secondOff = minOff * 60

def working_time(workTime):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < workTime:
        time.sleep(1)
        time_elapsed += 1

        time_left = workTime - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Time left: {minutes_left:02d}:{seconds_left:02d}")



def main(WorkTime, BreakTime):
    while True:

        working_time(WorkTime)

        pizzaTime = input("Its break time ! enter to continue (q to quit)")
        if pizzaTime == "q":
            break

        working_time(BreakTime)
        pizzaTime = input("Its work time ! enter to continue")
        if pizzaTime == "q":
            break




main(secondWork, secondOff)
