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


    index = 0
    total = list(set(boxes[0])| {0})
    added = True
    while added:
        added = False
        for j in join(boxes,total[index:]):
            if j not in total:
                total.append(j)
                index +=1
                added= True
    print(total)
    
    return len(total)==len(boxes)
