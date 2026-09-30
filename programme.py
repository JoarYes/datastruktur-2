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
calender = list([node] * 120)


print(calender)