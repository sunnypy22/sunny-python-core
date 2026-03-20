# Dataclass + TypedDict

from dataclasses import dataclass
from typing import TypedDict

@dataclass
class Point:
    x: float
    y: float

class StudentDict(TypedDict):
    name: str
    age: int

p = Point(3.5, 4.2)
print(p)

