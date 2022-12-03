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


def _get_group_shared_item(group_offset):
    return (
            set((x for x in data[group_offset]))
            & set((x for x in data[group_offset+1]))
            & set((x for x in data[group_offset+2]))
            ).pop()


def first():
    return sum([_get_priority(_get_compartments_shared_item(rucksack)) for rucksack in data])


def second():
    return sum([_get_priority(_get_group_shared_item(group_offset)) for group_offset in range(0, len(data), 3)])


data = get_input_data()
results(first, second)
