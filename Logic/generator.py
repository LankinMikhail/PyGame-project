import random


def generation(widht, height):
    walls = ["R", "D", "R", "D", "R", "D", "R", "D", "R", "D", "R", "D", "R", "D", "R", "D", ""]
    wallsR = ["R", ""]
    wallsD = ["D", ""]
    level1 = []
    lst = []
    for j in range(widht):
        lst.append(random.choice(wallsD))
    level1.append(lst)
    for i in range(height):
        lst = []
        for j in range(widht):
            lst.append(random.choice(walls))
        lst[-1] = ""
        lst[0] = random.choice(wallsR)
        level1.append(lst)
    level1.append([""] * widht)
    return level1
