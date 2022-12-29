# good candidate for consolidating/reducing lines of code
from main import get_input_data, results


def _border(row, column):
    return row == 0 or column == 0 or row == len(data)-1 or column == len(data[row])-1


def _visible(row, column):
    if _border(row, column):
        return True
    height = data[row][column]

    left_visible = True
    right_visible = True
    up_visible = True
    down_visible = True

    left_viewing_distance = 0
    right_viewing_distance = 0
    up_viewing_distance = 0
    down_viewing_distance = 0

    # check left
    c = column - 1
    while c >= 0:
        if data[row][c] >= height:
            left_visible = False
        else:
            left_viewing_distance += 1
        c -= 1

    # check right
    c = column + 1
    while c <= len(data[row])-1:
        if data[row][c] >= height:
            right_visible = False
        else:
            right_viewing_distance += 1
        c += 1

    # check up
    r = row - 1
    while r >= 0:
        if data[r][column] >= height:
            up_visible = False
        else:
            up_viewing_distance += 1
        r -= 1

    # check down
    r = row + 1
    while r <= len(data)-1:
        if data[r][column] >= height:
            down_visible = False
        else:
            down_viewing_distance += 1
        r += 1
    return left_visible or right_visible or up_visible or down_visible


def _num_trees_visible():
    num_trees_visible = 0
    for row in range(len(data)):
        for column in range(len(data[row])):
            if _visible(row, column):
                num_trees_visible += 1
    return num_trees_visible


def _max_scenic_score():
    max_scenic_score = 0
    for row in range(len(data)):
        for column in range(len(data[row])):
            s = _scenic_score(row, column)
            max_scenic_score = s if s > max_scenic_score else max_scenic_score
    return max_scenic_score


def _scenic_score(row, column):
    height = data[row][column]
    left_scenic_score = 0
    right_scenic_score = 0
    up_scenic_score = 0
    down_scenic_score = 0

    # check left
    c = column - 1
    while c >= 0 and data[row][c] <= height:
        left_scenic_score += 1
        if data[row][c] == height:
            break
        c -= 1

    # check right
    c = column + 1
    while c <= len(data[row])-1 and data[row][c] <= height:
        right_scenic_score += 1
        if data[row][c] == height:
            break
        c += 1

    # check up
    r = row - 1
    while r >= 0 and data[r][column] <= height:
        up_scenic_score += 1
        if data[r][column] == height:
            break
        r -= 1

    # check down
    r = row + 1
    while r <= len(data)-1 and data[r][column] <= height:
        down_scenic_score += 1
        if data[r][column] == height:
            break
        r += 1

    return left_scenic_score * right_scenic_score * up_scenic_score * down_scenic_score


def first():
    return _num_trees_visible()


def second():
    return _max_scenic_score()


data = get_input_data()
results(first, second)
