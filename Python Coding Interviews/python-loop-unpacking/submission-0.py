from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_scorer, highest_score = "", 0

    for x, y in scores:
        if y > highest_score:
            best_scorer = x
            highest_score = y
    
    return best_scorer

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
