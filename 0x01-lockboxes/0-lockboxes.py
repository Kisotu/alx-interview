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
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
