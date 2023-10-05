#!/usr/bin/python3
""" function that checks for unlocked boxes """


def canUnlockAll(boxes):
    """returns True if key unlocks """
    unlocked = [False] * len(boxes)
    unlocked[0] = True

    s = [0]

    while s:
        curr_box = s.pop()

        for key in boxes[curr_box]:
            if key >= 0 and key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                s.append(key)

    return all(unlocked)
