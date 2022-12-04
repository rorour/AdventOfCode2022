def get_input_data(file_name="./input", clean=True, to_int=False):
    def _clean(line):
        return line.rstrip('\n')

    def _to_int(line):
        if len(line) > 0:
            return int(line)
        return None

    def _process(line):
        line = _clean(line) if clean else line
        line = _to_int(line) if to_int else line
        return line

    with open(file_name, "r") as infile:
        data = [_process(line) for line in infile]
    return data


def results(first, second):
    print(f"first puzzle: {first()}")
    print(f"second puzzle: {second()}")
