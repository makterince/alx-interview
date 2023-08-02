#!/usr/bin/python3

def canUnlockAll(boxes):
    """
       Determine if all boxes can be opened.
       Args:
            boxes (list[list[int]]): A list of lists representing the boxes and their contained keys.
       Returns:
            bool: True if all boxes can be opened, False otherwise.
    """


    visited = [False] * len(boxes)
    visited[0] = True
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)
                
    return all(visited)
