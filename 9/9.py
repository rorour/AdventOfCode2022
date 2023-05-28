from main import get_input_data, results


def _calculate_for_rope(num_tails):
    _TAILS = ["T" + str(n) for n in range(1, num_tails + 1)]
    instructions = _clean_instructions()
    starting_positions = {}
    for k in _TAILS + ["H"]:
        starting_positions[k] = (0, 0)
    positions = {"s": starting_positions}
    prev_position = positions["s"]
    step = 0
    for n in instructions:
        direction, number = n
        for s in range(number):
            h = _calculate_h(direction, prev_position["H"])
            p = {"H": h}
            prev_knot = "H"
            for t in _TAILS:
                p[t] = _calculate_t(p[prev_knot], prev_position[t])
                prev_knot = t
            positions[step] = p
            prev_position = positions[step]
            step += 1
    return _count_unique_positions(positions, _TAILS[-1])


def _calculate_h(direction, prev_position):
    if direction == "U":
        return prev_position[0], prev_position[1] + 1
    elif direction == "D":
        return prev_position[0], prev_position[1] - 1
    elif direction == "L":
        return prev_position[0] - 1, prev_position[1]
    elif direction == "R":
        return prev_position[0] + 1, prev_position[1]


def _calculate_t(h, prev_position):
    def _check_diagonal_x():
        if h[0] - prev_position[0] == 1:
            t[0] = t[0] + 1
        if prev_position[0] - h[0] == 1:
            t[0] = t[0] - 1

    def _check_diagonal_y():
        if h[1] - prev_position[1] == 1:
            t[1] = t[1] + 1
        if prev_position[1] - h[1] == 1:
            t[1] = t[1] - 1

    t = [prev_position[0], prev_position[1]]
    if h[1] - prev_position[1] == 2:
        t[1] = t[1] + 1
        _check_diagonal_x()
    if h[0] - prev_position[0] == 2:
        t[0] = t[0] + 1
        _check_diagonal_y()
    if prev_position[0] - h[0] == 2:
        t[0] = t[0] - 1
        _check_diagonal_y()
    if prev_position[1] - h[1] == 2:
        t[1] = t[1] - 1
        _check_diagonal_x()
    return t[0], t[1]


def _clean_instructions():
    instructions = []
    for line in data:
        s = line.split(" ")
        s[-1] = int(s[-1])
        instructions.append(s)
    return instructions


def _count_unique_positions(positions, key):
    return len(set([v[key] for v in positions.values()]))


def first():
    return _calculate_for_rope(1)


def second():
    return _calculate_for_rope(9)


data = get_input_data(file_name="input")
results(first, second)
