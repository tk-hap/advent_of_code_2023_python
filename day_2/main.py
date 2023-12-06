import re

with open("day_2/input.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        split_line = re.split(": |; ", line)
        game_id = int(split_line.pop(0).removeprefix("Game "))

        for set in split_line:
            set_values = re.split(" |, ", set)
            values = [int(x) for x in set_values if x.isdigit()]
            keys = [x for x in set_values if not x.isdigit()]
            set_dictionary = dict(zip(keys, values))

            #TODO check color values
            if set_dictionary["red"] > red_val
            print(set_dictionary)