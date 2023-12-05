FILE = "day_1/input.txt"

STRING_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}
ALL_NUMBERS = []


def create_number(numbers_in_line: list) -> bool:
    first_number = STRING_DIGITS[numbers_in_line[0]]
    last_number = STRING_DIGITS[numbers_in_line[-1]]
    number = int(f"{first_number}{last_number}")
    ALL_NUMBERS.append(number)
    return True


def sort_by_index(numbers_in_line: dict) -> list:
    keys = list(numbers_in_line.keys())
    keys.sort()
    sorted_dict = {i: numbers_in_line[i] for i in keys}
    return list(sorted_dict.values())


with open(FILE, "r") as f:
    lines = f.readlines()

    for line in lines:
        numbers_in_line = {}

        for key in STRING_DIGITS.keys():
            if key in line:
                i = 0
                # Handle multiples of the same number
                while i < len(line):
                    found_index = line.find(key, i)
                    if found_index == -1:
                        break
                    else:
                        numbers_in_line[found_index] = key
                    i += 1

        numbers_in_line = sort_by_index(numbers_in_line)
        create_number(numbers_in_line)

print(sum(ALL_NUMBERS))
