# Using type annotations (Python 3.5+)
from typing import List, Tuple, Optional
def calculate_average(numbers: List[float]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
def find_person(people: List[Tuple[str, int]], name: str) -> Optional[int]:
    for person_name, age in people:
        if person_name == name:
            return age
    return None
scores = [85.5, 92.0, 78.5, 90.0]
print("Average:", calculate_average(scores))
team = [("Sunny", 25), ("Priya", 19), ("Rahul", 22)]
print("Age of Priya:", find_person(team, "Priya"))
print("Age of Neha:", find_person(team, "Neha"))   # None