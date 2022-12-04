from main import get_input_data, results


def _get_calorie_totals():
    calorie_totals = []
    single_elf_total = 0
    for line in data:
        if line is None:
            calorie_totals.append(single_elf_total)
            single_elf_total = 0
        else:
            single_elf_total += line
    calorie_totals.append(single_elf_total)
    return calorie_totals


def first():
    return max(_get_calorie_totals())


def second():
    return sum(sorted(_get_calorie_totals())[-3:])


data = get_input_data(to_int=True)
results(first, second)
