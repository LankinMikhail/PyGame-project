import random


def generation(width, height):
    walls = ["R", "D", "R", "D", "R", "D", "R", "D", "R", "D", "R", "D", "R", "D", "R", "D", ""]
    wallsR = ["R", ""]
    wallsD = ["D", ""]
    level1 = []
    lst = []
    for j in range(width):
        lst.append(random.choice(wallsD))
    level1.append(lst)
    for i in range(height - 1):
        lst = []
        for j in range(width):
            lst.append(random.choice(walls))
        lst[-1] = ""
        lst[0] = random.choice(wallsR)
        level1.append(lst)
    level1.append([""] * width)
    return level1


def random_place(width, height, cell_size, left, top, already):
    randx = random.randint(1, width) * cell_size - cell_size // 2 + left
    randy = random.randint(1, height) * cell_size - cell_size // 2 + top
    randangle = random.randint(0, 359)
    if (randx, randy) in already:
        return random_place(width, height, cell_size, left, top, already)
    else:
        return randx, randy, randangle
