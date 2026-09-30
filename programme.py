from dataclasses import dataclass
from datetime import date


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

def addMonthDateNodes(c, day, days):
    if day == days-1: 
        c = Node(None, None)
        return c
    else:
        day += 1
        c.node = Node(None, addMonthDateNodes(c, day, days))
        return c.node

offset = 0
yearCheck = False

for i in range(120):

    print(i)
    if i > 8 and yearCheck == False:
        offset -= 1
        yearCheck = True
    
    if (i - offset) % 2 == 0:
        calender[i].node = addMonthDateNodes(calender[i], 1, 31)
        print("hello")
    elif (i - offset) % 2 != 0:
        calender[i].node = addMonthDateNodes(calender[i], 1, 30)
        print("goodbay")

    if i % 12 == 0:
        yearCheck = False


print(calender)
