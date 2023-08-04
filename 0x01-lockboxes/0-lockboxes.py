#!/usr/bin/python3
""" this module contains a function that checks if boxes can be unlocked"""

def canUnlockAll(boxes):
    """
       Determine if all boxes can be opened.
       Args:
            boxes (list[list[int]]): A list of lists representing the boxes and their contained keys.
       Returns:
            bool: True if all boxes can be opened, False otherwise.
    """

    # Initialize the current index to 0 and create a set containing box 0
    index = 0
    total = list(set(boxes[0])| {0})
    added = True
    while added:
        added = False
        # Iterate through keys in the current box and add them to the set
        for j in join(boxes,total[index:]):
            if j not in total:
                total.append(j)
                index +=1
                added= True
    print(total)

    # Return True if the number of opened boxes is equal to the total number of boxes
    return len(total)==len(boxes)
