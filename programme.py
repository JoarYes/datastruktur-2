from dataclasses import dataclass
from datetime import datetime, date


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

def addMonthDateNodes(c, day, amount):
    if day == amount-1: 
        c = Node(None, None)
        return c
    else:
        day += 1
        c.node = Node(None, addMonthDateNodes(c, day, amount))
        return c.node

def searchSession(target, currentNode):
    print(currentNode.session.Date.day, target.day)
    if target.day == currentNode.session.Date.day:
        if currentNode.node == None:
            return [currentNode.session]
        elif target.day == currentNode.node.session.Date.day:
            anotherSession = searchSession(target, currentNode.node)

            # Used for searching more than 2 nodes
            if type(anotherSession) == list:
                currentList = []

                for i in range(len(anotherSession)):
                    indexSession = anotherSession[i]

                    currentList[i+1] = indexSession
                return currentList

            sessionList = [currentNode.session, anotherSession]
            return sessionList
        return [currentNode.session]
    else:
        try:
            anotherSession = searchSession(target, currentNode.node)

            if type(anotherSession) == list:
                currentList = []

                for i in range(len(anotherSession)):
                    print(i)
                    print(anotherSession)
                    indexSession = anotherSession[i]

                    currentList[i] = indexSession
                return currentList

            sessionList = [anotherSession]
            return sessionList
        except Exception as e:
            print(f"\n {e} \n")
            print("Sessions for this date does not exist\n")
            return None

def printSession(sessionList):
    pass

# Insert session into correct spot
def addNode(aSession, prevNode):
    pointer = prevNode.node

    if prevNode.session == None:
        prevNode.session = aSession
        return None

    if prevNode.node == None:
        if aSession.Date.day <= prevNode.session.Date.day:
            pointer = Node(prevNode.session, prevNode.node)

            prevNode.session = aSession
            prevNode.node = pointer
            
            return None
        
        prevNode.node = Node(aSession, pointer)
        return None
    
    # Compares session day with current and next node
    if aSession.Date.day >= prevNode.session.Date.day:
        if aSession.Date.day < prevNode.node.session.Date.day:
            prevNode.node = Node(aSession, pointer)
            return None
        else:
            node = addNode(aSession, prevNode.node)
            
    elif aSession.Date.day < prevNode.session.Date.day:
        pointer = Node(prevNode.session, prevNode.node)
        
        prevNode.session = aSession
        prevNode.node = pointer
        
        return None
    else:
        try:
            node = addNode(aSession, prevNode.node)
        except:
            return None

    return node

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
        while True:
            try:
                dateInput = datetime.strptime(input("What date(DD.MM.YYYY): "),"%d.%m.%Y").date()
            except:
                print("Invalid input!")
                continue

            if dateInput.year > 2035 or dateInput.year < 2026:
                print("Year must be between 2026 and 2035!")
                continue

            descriptionInput = input("Description: ")

            try:
                lengthInput = float(input("Length ran(km.m): "))
            except:
                print("Invalid input!\nTry again!\n")
                continue
            
            durationInput = input("Duration(H.M.S): ").split(".")
            try:
                duration = Duration(durationInput[0], durationInput[1], durationInput[2])
            except:
                print("Invalid input!")
                continue

            newSession = Session(dateInput, descriptionInput, lengthInput, duration)

            startYear = 2026
            startMonth = 1

            # Calculate proper index
            index = (dateInput.year - startYear) * 12 + (dateInput.month - startMonth)

            addNode(newSession, calender[index])
            print(calender[index])
            print("Session successfully added\n")
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
            print(calender[index])
            sessionsList = searchSession(dateInput, calender[index])

            print(sessionsList)
            break