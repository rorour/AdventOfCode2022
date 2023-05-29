from main import get_input_data, results


def _get_least_common_multiple(monkeys):
    divisors = []
    for m in monkeys.values():
        divisors.append(int(m["test"].strip("divisible by ")))
    r = 1
    for d in divisors:
        r *= d
    return r


def _monkey_business(monkeys):
    i = sorted([m['inspections'] for m in monkeys.values()])
    return i[-1] * i[-2]


def _operation(item, instruction, lcm):
    if instruction.startswith("new = old * "):
        v = instruction.split("* ")[-1]
        if v == "old":
            return (item * item) % lcm
        v = int(v)
        return (item * int(v)) % lcm
    elif instruction.startswith("new = old + "):
        v = instruction.split("+ ")[-1]
        if v == "old":
            return (item + item) % lcm
        v = int(v)
        return (item + v) % lcm
    else:
        raise NotImplementedError(instruction)


def _parse_input():
    monkeys = {}
    for i, line in enumerate(data):
        if line.startswith("Monkey"):
            monkeys[line.split(" ")[-1].strip(":")] = {
                "items": [int(x) for x in data[i + 1].split(":")[-1].split(",")],
                "operation": data[i + 2].split(": ")[-1], "test": data[i + 3].split(": ")[-1],
                "true_throw": data[i + 4].split("throw to monkey ")[-1],
                "false_throw": data[i + 5].split("throw to monkey ")[-1],
                "inspections": 0,
            }
    return monkeys


def _test(new_worry_level, test):
    assert test.startswith("divisible by ")
    d = int(test.strip("divisible by "))
    return new_worry_level % d == 0


def _throw(monkey_from, monkey_to, item, monkeys):
    monkeys[monkey_from]["items"] = monkeys[monkey_from]["items"][1:]
    monkeys[monkey_to]["items"] = monkeys[monkey_to]["items"] + [item]


def _turn(monkeys, monkey_num, monkey, part_two=False):
    for item in monkey["items"]:
        monkey["inspections"] = monkey["inspections"] + 1
        item = _operation(item, monkey["operation"], _get_least_common_multiple(monkeys))
        if not part_two:
            item //= 3
        if _test(item, monkey["test"]):
            _throw(monkey_num, monkey["true_throw"], item, monkeys)
        else:
            _throw(monkey_num, monkey["false_throw"], item, monkeys)


def first():
    monkeys = _parse_input()
    for r in range(20):
        for monkey_num, monkey in sorted(monkeys.items()):
            _turn(monkeys, monkey_num, monkey)
    return _monkey_business(monkeys)


def second():
    monkeys = _parse_input()
    for r in range(10000):
        for monkey_num, monkey in sorted(monkeys.items()):
            _turn(monkeys, monkey_num, monkey, part_two=True)
    return _monkey_business(monkeys)


data = get_input_data(file_name="input")
results(first, second)
