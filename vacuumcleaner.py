def printInformation(location):
    print(f"Location {location} is Dirty.")
    print(f"Cost for CLEANING {location}: 1")
    print(f"Location {location} has been Cleaned.")


def vacuumCleaner(goalState, currentState, location):
    print("Goal State Required:", goalState)
    print(f"Vacuum is placed in Location {location}")

    totalCost = 0

    while currentState != goalState:
        if location == "A":
            if currentState["A"] == 1:
                currentState["A"] = 0
                totalCost += 1
                printInformation("A")
            if currentState["B"] == 1:
                print("Moving right to the location B.")
                location = "B"

        elif location == "B":
            if currentState["B"] == 1:
                currentState["B"] = 0
                totalCost += 1
                printInformation("B")
            if currentState["A"] == 1:
                print("Moving left to the location A.")
                location = "A"

    print("GOAL STATE:", currentState)
    return totalCost

goalState = {"A": 0, "B": 0}
currentState = {"A": -1, "B": -1}

location = input("Enter Location of Vacuum (A/B): ")
currentState["A"] = int(input("Enter status of A (0/1): "))
currentState["B"] = int(input("Enter status of B (0/1): "))

totalCost = vacuumCleaner(goalState, currentState, location)
print("Performance Measurement:", totalCost)

