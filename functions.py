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

def addMonthDateNodes(c, day, amount):
    if day == amount-1: 
        c = Node(None, None)
        return c
    else:
        day += 1
        c.node = Node(None, addMonthDateNodes(c, day, amount))
        return c.node

def searchSession(target, currentNode):
    if currentNode.session == None:
        print("Sessions for this date does not exist\n")
        return None
    
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

                    currentList.append(indexSession)

                currentList.append(currentNode.session)
                return currentList
        return [currentNode.session]
    else:
        try:
            anotherSession = searchSession(target, currentNode.node)

            if type(anotherSession) == list:
                currentList = []

                for i in range(len(anotherSession)):
                    indexSession = anotherSession[i]

                    currentList.append(indexSession)
                return currentList

            sessionList = [anotherSession]
            return sessionList
        except Exception as e:
            print("Sessions for this date does not exist\n")
            return None

# Prints sessions in a easy to read way
def printSession(sessionList):
    for i in range(len(sessionList)):
        session = sessionList[i]

        print(f"\n{i+1}.\n" + "Date: " + str(session.Date.day) + "." + str(session.Date.month) + "." + str(session.Date.year))
        print("Length: " + str(session.length) + "km")
        print("Duration: " + str(session.time.hour) + "h", str(session.time.minute) + "m", str(session.time.second) + "s")
        print("Description: " + session.description + "\n")

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

def deleteSession(target, headNode):
    if target == None or target == [None]:
        return None
    
    result = searchSession(target[0].Date, headNode)

    if result == None:
        return None
    else:
        while True:
            result = searchSession(target[0].Date, headNode)
            printSession(result)
            print("Press only enter to cancel command.")
            usrInput = input("Which session do you want to delete?(number) ")

            if usrInput == "":
                return None
            else:
                try:
                    usrInput = int(usrInput)
                except:
                    print("Invalid input!")
                    continue

                try:
                    nodeDelete = target[usrInput - 1]
                except:
                    print("Session number does not exist!")
                    continue

                dSearchNode(nodeDelete, headNode, None)
                break

# Searches for the node that is to be deleted
def dSearchNode(target, currentNode, prevNode):
    if target == currentNode.session and prevNode == None:

        # Creates variable with the pointer to replace head node
        if currentNode.node != None:
            replaceNode = Node(currentNode.node.session, currentNode.node.node)
        else:
            replaceNode = Node(None, None)

        # Confirm deletion by user
        while True:
            cancel = input("Do you want to delete this session?(y/n) ")
            if cancel == "y":
                pass
            elif cancel == "n":
                return None
            else:
                print("Invalid input!")
                continue
            break

        currentNode.session = replaceNode.session
        currentNode.node = replaceNode.node
        print("Session successfuly deleted.")
        return None
    elif target == currentNode.session:
        if currentNode.node != None:
            replaceNode = Node(currentNode.node.session, currentNode.node.node)
        else:
            replaceNode = None

        # Confirm deletion by user
        while True:
            cancel = input("Do you want to delete this session?(y/n) ")
            if cancel == "y":
                pass
            elif cancel == "n":
                return None
            else:
                print("Invalid input!")
                continue
            break

        prevNode.node = replaceNode

    else:
        dSearchNode(target, currentNode.node, currentNode)