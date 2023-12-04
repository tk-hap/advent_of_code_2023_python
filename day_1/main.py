import os
import string

FILE = "input.txt"
DIGITS = string.digits
ALL_NUMBERS = []

def create_number(numbers_in_line: list) -> None:
    number = numbers_in_line[0] + numbers_in_line[-1]
    ALL_NUMBERS.append(int(number))

with open(FILE, "r") as f:
    lines = f.readlines()
    for line in lines:
        numbers_in_line = [x for x in line if x in DIGITS]
        create_number(numbers_in_line)

print(sum(ALL_NUMBERS))

             