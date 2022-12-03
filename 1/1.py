from main import get_input_data, results


def _get_calorie_totals():
    calorie_totals = []
    x = 0
    for l in data:
        if l is None:
            calorie_totals.append(x)
            x = 0
        else:
            x += l
    calorie_totals.append(x)
    return calorie_totals


def first():
    return max(_get_calorie_totals())


def second():
    return sum(sorted(_get_calorie_totals())[-3:])


data = get_input_data(to_int=True)
results(first, second)
