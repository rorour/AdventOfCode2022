from main import get_input_data, results


def _ranges_overlap(first_min, first_max, second_min, second_max):
    return (second_min <= first_min <= second_max) or (
                second_min <= first_max <= second_max) or _fully_contained_range(first_min, first_max, second_min, second_max)


def _fully_contained_range(first_min, first_max, second_min, second_max):
    return (first_min <= second_min and first_max >= second_max) or (first_min >= second_min and first_max <= second_max)


def _get_min_maxes(line):
    return [int(x) for x in line.split(',')[0].split('-')] + [int(x) for x in line.split(',')[1].split('-')]


def first():
    return len([line for line in data if _fully_contained_range(*_get_min_maxes(line))])


def second():
    return len([line for line in data if _ranges_overlap(*_get_min_maxes(line))])


data = get_input_data()
results(first, second)
