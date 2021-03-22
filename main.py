import matplotlib.pyplot as plt

# initDoors() returns a list of what's behind three doors, one of which has been randomly selected to be a car

# chooseDoor() randomly chooses on of the three doors (origChoice)

# openDoor() randomly chooses one of the one or two doors containing a goat that haven't been selected

# result() returns True if the car was behind the originalChoice door, and false otherwise

def plotResult(origChoiceWins, changeWins):
    '''(int, int) -> None
    Creates a pie chart of the results.
    '''
    results = [origChoiceWins, changeWins]
    labels = ["Wins from original choice", "Wins from changing choice"]
    colours = ["royalblue", "slategrey"]
    plt.pie(results, labels=labels, colors=colours, startangle=90)
    plt.title("Monty Hall Simulation")
    plt.show()

# in main(), make a loop of 1000 tests
# if result() == True, add one to originalChoiceWins, else add one to changeWins

plotResult(50, 120)
