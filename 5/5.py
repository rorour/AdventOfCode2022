from main import get_input_data, results


stacks = {}
instructions = []


def _set_stacks():
    global stacks
    global instructions
    stacks = {}
    instructions = []
    for i, line in enumerate(data):
        if line == '':
            instructions = data[i + 1:]
            break
        for j, crate in enumerate([line[j:j + 3] for j in range(0, len(line), 4)], 1):
            if '[' in crate:
                a = stacks.get(j, [])
                a.append(crate[1])
                stacks[j] = a


def _move_crates(one_at_a_time):
    global stacks
    global instructions

    _set_stacks()
    for m in instructions:
        m = m.split(' ')
        for i in range(int(m[1])):
            crate = stacks[int(m[3])].pop(0)
            stacks[int(m[5])].insert(0 if one_at_a_time else i, crate)
    top_crates = ''
    for k in sorted(stacks.keys()):
        top_crates += stacks[k][0]
    return top_crates


def first():
    return _move_crates(one_at_a_time=True)


def second():
    return _move_crates(one_at_a_time=False)


data = get_input_data()
results(first, second)
