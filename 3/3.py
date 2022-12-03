from main import get_input_data, results


def _get_priority(item):
    if item == item.lower():
        return ord(item) - 96
    return ord(item) - 38


def _get_compartments_shared_item(rucksack):
    items = {}
    for item in rucksack[:len(rucksack) // 2]:
        items[item] = True
    for item in rucksack[len(rucksack) // 2:]:
        if items.get(item):
            return item


def first():
    return sum([_get_priority(_get_compartments_shared_item(rucksack)) for rucksack in data])


def second():
    priority_sum = 0
    for i in range(0, len(data), 3):
        shared_item = (set((x for x in data[i])) & set((x for x in data[i+1])) & set((x for x in data[i+2]))).pop()
        priority_sum += _get_priority(shared_item)
    return priority_sum


data = get_input_data()
results(first, second)
