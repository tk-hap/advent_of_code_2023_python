import re

game_list = []


def check_set(set_dictionary: dict) -> bool:
    red = 12
    green = 13
    blue = 14

    if set_dictionary.get("red", 0) > red:
        print("Too many reds")
        return False
    elif set_dictionary.get("green", 0) > green:
        print("Too many greens")
        return False
    elif set_dictionary.get("blue", 0) > blue:
        print("Too many blues")
        return False
    else:
        return True


with open("day_2/input.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        split_line = re.split(": |; ", line)
        game_id = int(split_line.pop(0).removeprefix("Game "))
        game_list.append(game_id)

        for set in split_line:
            set_values = re.split(" |, ", set)
            values = [int(x) for x in set_values if x.isdigit()]
            keys = [x for x in set_values if not x.isdigit()]
            set_dictionary = dict(zip(keys, values))

            if not check_set(set_dictionary):
                game_list.remove(game_id)
                break


print(game_list)
print(sum(game_list))
