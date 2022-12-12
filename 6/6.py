from main import get_input_data, results


def _characters_parsed_for_marker(case):
    if case == 'packet':
        marker_length = 4
    elif case == 'message':
        marker_length = 14
    else:
        raise ValueError

    datastream = data[0]
    for i in range(len(datastream) - marker_length + 1):
        section = datastream[i:i + marker_length]
        if len(set(section)) == len(section):
            return i + marker_length


def first():
    return _characters_parsed_for_marker('packet')


def second():
    return _characters_parsed_for_marker('message')


data = get_input_data()
results(first, second)
