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
augustCheck = False
yearCheck = False

for i in range(120):

    calender[i] = Node(None, None)


print(calender)
