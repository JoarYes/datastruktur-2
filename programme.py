from dataclasses import dataclass
from datetime import datetime, date
from functions import addNode, searchSession, deleteSession, printSession


@dataclass
class Duration:
    hour: int
    minute: int
    second: int

@dataclass
class Session:
    Date: date
    description: str
    length: int
    time: Duration


@dataclass
class Node:
    session: Session | None
    node: Node | None

# calender[0] = januari 2026
# calender[119] = december 2035

node = Node(None, None)
calender = [Node(None, None) for _ in range(120)] 

offset = 0
augustCheck = False
yearCheck = False

for i in range(120):

    calender[i] = Node(None, None)

# User inputs
while True:

    print("What do you want to do?")
    print("Add session (a), Delete session (d), List sessions (l)")

    usrInput = input("Command: ")

    # Add session
    if usrInput == "a":
        print("\nEnter an invalid input to choose whether to stop or continue current command.")
        while True:
            try:
                dateInput = datetime.strptime(input("What date(DD.MM.YYYY): "),"%d.%m.%Y").date()
            except:
                print("Invalid input!")

                # Checks if the user wants to cancel current command
                cancel = input("Cancel current command?(x): ")
                if cancel == "x":
                    break
                continue

            if dateInput.year > 2035 or dateInput.year < 2026:
                print("Year must be between 2026 and 2035!")

                # Checks if the user wants to cancel current command
                cancel = input("Cancel current command?(x): ")
                if cancel == "x":
                    break
                continue

            descriptionInput = input("Description: ")

            try:
                lengthInput = float(input("Length ran(km.m): "))
            except:
                print("Invalid input!")

                # Checks if the user wants to cancel current command
                cancel = input("Cancel current command?(x): ")
                if cancel == "x":
                    break
                continue
            
            durationInput = input("Duration(H.M.S): ").split(".")
            try:
                duration = Duration(int(durationInput[0]), int(durationInput[1]), int(durationInput[2]))
            except:
                print("Invalid input!")

                # Checks if the user wants to cancel current command
                cancel = input("Cancel current command?(x): ")
                if cancel == "x":
                    break
                continue

            newSession = Session(dateInput, descriptionInput, lengthInput, duration)

            startYear = 2026
            startMonth = 1

            # Calculate proper index
            index = (dateInput.year - startYear) * 12 + (dateInput.month - startMonth)

            addNode(newSession, calender[index])
            print("Session successfully added\n")
            break

    if usrInput == "d":
        while True:
            try:
                print("\nEnter an invalid input to choose whether to stop or continue current command.")
                dateInput = datetime.strptime(input("What date(DD.MM.YYYY): "),"%d.%m.%Y").date()
            except:
                print("Invalid input!\n")
                break

            if dateInput.year > 2035 or dateInput.year < 2026:
                print("Year must be between 2026 and 2035!")
                continue

            startYear = 2026
            startMonth = 1

            # Calculate proper index
            index = (dateInput.year - startYear) * 12 + (dateInput.month - startMonth)

            sessionsList = searchSession(dateInput, calender[index])

            deleteSession(sessionsList, calender[index])
            break

    # List session(s)
    if usrInput == "l":
        while True:
            try:
                dateInput = datetime.strptime(input("What date(DD.MM.YYYY): "),"%d.%m.%Y").date()
            except:
                print("Invalid input!\n")
                continue

            if dateInput.year > 2035 or dateInput.year < 2026:
                print("Year must be between 2026 and 2035!")
                continue

            startYear = 2026
            startMonth = 1

            # Calculate proper index
            index = (dateInput.year - startYear) * 12 + (dateInput.month - startMonth)

            sessionsList = searchSession(dateInput, calender[index])

            if sessionsList != None:
                if sessionsList == [None]:
                    break
                printSession(sessionsList)

            break