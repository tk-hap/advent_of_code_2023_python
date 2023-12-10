import re

def valid_pos(i, j, n, m):
 
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1
 

def get_adjacent(arr, i, j):
 
    # Size of given 2d array
    n = len(arr)
    m = len(arr[0])
 
    v = []
 
    # Checking for all the possible adjacent positions
    if (valid_pos(i - 1, j - 1, n, m)):
        if arr[i - 1][j - 1] == "*":
            v.append(f'{i -1}{j -1}')
    if (valid_pos(i - 1, j, n, m)):
        if arr[i - 1][j] == "*":
            v.append(f'{i -1}{j}')
    if (valid_pos(i - 1, j + 1, n, m)):  
        if arr[i - 1][j + 1] == "*":
            v.append(f'{i -1}{j +1}')
    if (valid_pos(i, j - 1, n, m)):
        if arr[i][j - 1] == "*":
            v.append(f'{i}{j -1}')
    if (valid_pos(i, j + 1, n, m)):
        if arr[i][j + 1] == "*":
            v.append(f'{i}{j +1}')
    if (valid_pos(i + 1, j - 1, n, m)):
        if arr[i + 1][j - 1] == "*":
            v.append(f'{i +1}{j -1}')
    if (valid_pos(i + 1, j, n, m)):
         if arr[i + 1][j] == "*":
             v.append(f'{i +1}{j}')
    if (valid_pos(i + 1, j + 1, n, m)):
        if arr[i + 1][j + 1] == "*":
            v.append(f'{i +1}{j +1}')
 
    return v


regex = re.compile('[0-9]+')
found_nums = {}

with open("day_3/input.txt", "r") as f:
    lines = f.read().splitlines()
    grid = [list(x) for x in lines]
    for row in grid:
        print(row) 
    for counter, line in enumerate(lines):
        regex_iter = regex.finditer(line)
        for match in regex_iter:
            gears = set()
            print(f"Checking {match}")
            num = int(match.group(0))
            for i in range(match.start(), match.end()):
                gears.update(get_adjacent(grid, counter, i))
            
            gears_index = list(gears)

            if len(gears_index) > 0:
                if gears_index[0] in found_nums:
                    found_nums[gears_index[0]].append(num)
                else:
                    found_nums[gears_index[0]] = [num]
            print(gears)

totals = []
for k, v in found_nums.items():
    if len(v) == 2:
        totals.append(v[0] * v[1])
print(totals)
print(sum(totals))