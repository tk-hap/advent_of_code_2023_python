import re

powers = []


def count_colours(set_dictionary: dict):
    #Add to totals
    for key, value in colour_totals.items():
        if value < set_dictionary.get(key, 0):
            colour_totals[key] = set_dictionary.get(key)



with open("day_2/input.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        split_line = re.split(": |; ", line)
        colour_totals = {"red": 0, "green": 0, "blue": 0}

        for set in split_line:
            set_values = re.split(" |, ", set)
            values = [int(x) for x in set_values if x.isdigit()]
            keys = [x for x in set_values if not x.isdigit()]
            set_dictionary = dict(zip(keys, values))
            count_colours(set_dictionary)

        powers.append(colour_totals["red"] * colour_totals["blue"] * colour_totals["green"])


print(powers)
print(sum(powers))
