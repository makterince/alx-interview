#!/usr/bin/env python3
"""
This module contains a function that checks if boxes can be unlocked.
"""

def can_unlock_all(boxes):
        """
        Determine if all boxes can be opened.
        Args:
            boxes (list[list[int]]): A list of lists representing the boxes and their contained keys.
        Returns:
            bool: True if all boxes can be opened, False otherwise.
        """


        index = 0
        total = set(boxes[0]) | {0}  # Start with keys from box 0 and box 0 itself
        added = True
        
        while added:
            added = False
            for j in join(boxes, total[index:]):
                if j not in total:
                    total.add(j)
                    index += 1
                    added = True
                    
        return len(total) == len(boxes)
    
    def join(boxes, indices):
    """
    Helper function to iterate through the boxes and get keys from indices.
    Args:
        boxes (list[list[int]]): A list of lists representing the boxes and their contained keys.
        indices (list[int]): List of indices to get keys from.
    Yields:
        int: Key value from specified indices.
    """
    for i in indices:
        for key in boxes[i]:
            yield key
