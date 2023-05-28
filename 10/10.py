from main import get_input_data, results


def _clean_instructions():
    for line in data:
        l = line.split(" ")
        if len(l) == 2:
            l[1] = int(l[1])
        yield l


def _is_interesting_signal(cycle):
    return cycle == 20 or (cycle - 20) % 40 == 0


def first():
    CRT = open("CRT", "w")
    instructions = _clean_instructions()
    register_X = 1
    cycle = 0
    interesting_signal_strengths = []
    in_progress = None  # [wait, op, value]

    while True:
        cycle += 1
        if abs(register_X - (cycle % 40 - 1)) < 2:
            CRT.write("#")
        else:
            CRT.write(".")
        if cycle % 40 == 0:
            CRT.write("\n")
        if _is_interesting_signal(cycle):
            interesting_signal_strengths.append(cycle * register_X)
        if in_progress is not None:
            in_progress[0] = in_progress[0] - 1
            if in_progress[0] == 0:
                register_X = register_X + in_progress[2]
                in_progress = None
            continue
        try:
            i = next(instructions)
            if i[0] == "noop":
                continue
            elif i[0] == "addx":
                in_progress = [1, i[0], i[1]]
                continue
        except StopIteration:
            break
    CRT.close()
    return sum(interesting_signal_strengths)


def second():
    return "see CRT"


data = get_input_data(file_name="input")
results(first, second)
