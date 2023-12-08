import re
import string

def check_grid(row, column, column_end=None):
    if column_end:
        if column > 0:
            column -= 1
        if column_end < len(grid[row])-1:
            column_end += 1
        results = grid[row][column:column_end]
    else: 
        results = grid[row][column]
    print(results)

    for result in results:
        if result not in string.digits and result != ".":
            print("Symbol found!")
            return True
    return False


regex = re.compile('[0-9]+')
found_nums = []

with open("day_3/input.txt", "r") as f:
    lines = f.read().splitlines()
    grid = [list(x) for x in lines]
    for row in grid:
        print(row) 
    for counter, line in enumerate(lines):
        regex_iter = regex.finditer(line)
        for match in regex_iter:
            print(f"Checking {match}")
            checks = []

            if match.start() > 0:
                checks.append(check_grid(row=counter, column=match.start()-1))

            if match.end() < len(line):
                checks.append(check_grid(row=counter, column=match.end()))
            if counter != 0:
                checks.append(check_grid(row=counter-1, column=match.start(), column_end=match.end()))
            if counter != len(lines)-1:
                checks.append(check_grid(row=counter+1, column=match.start(), column_end=match.end()))
            if any(checks):
                print(f"Adding {match.group(0)} to list")
                found_nums.append(int(match.group(0)))
            else:
                print(f"Skipping {match.group(0)}")

print(found_nums)
print(sum(found_nums))