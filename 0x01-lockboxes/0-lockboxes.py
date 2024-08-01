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
    leng = len(boxes)
    visit_boxes = set([0])
    unvisited_boxes = set(boxes[0]).difference(set([0]))
    while len(unvisited_boxes) > 0:
        boxIndex = unvisited_boxes.pop()
        if not boxIndex or boxIndex >= leng or boxIndex < 0:
            continue
        if boxIndex not in visit_boxes:
            unvisited_boxes = unvisited_boxes.union(boxes[boxIndex])
            visit_boxes.add(boxIndex)
    return leng == len(visit_boxes)
