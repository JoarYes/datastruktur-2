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
    duration: Duration
    session: Session
    node: Node | None