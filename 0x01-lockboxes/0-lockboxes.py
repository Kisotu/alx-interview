#!/usr/bin/python3

"""Python code that determines if locked boxws can be opened"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists, where each inner list represents a box
            containing keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if len(boxes) == 0:
        return True

    queue = [0]
    visited = set()

    while queue:
        box = queue.pop(0)

        if box in visited:
            continue

        visited.add(box)

        for key in range(len(boxes[box])):
            new_box = boxes[box][key]

            if new_box in visited:
                continue

            if new_box >= len(boxes):
                return False

            queue.append(new_box)
    return True
