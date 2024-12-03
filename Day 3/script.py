import re

f = open('list.txt', 'r')

content = f.read()

# Part 1 : Find the mul() instructions in the file, and execute them. ignore all other characters.
# Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# example: 07)[#;mul(725,121) %[>mul(115,425)${what()mul(219,305)how()])

# regex: mul\((\d+),(\d+)\)
# match mul then the ( character, then one or more digits 0-9, then a comma, then one or more digits 0-9, then the ) character.

mulMatch = (re.findall(r'mul\((\d+),(\d+)\)', content))

mulMatch = [(int(x), int(y)) for x, y in mulMatch]

print(mulMatch)

total = 0
for x, y in mulMatch:
    total += x * y
    
print("Total is: ", total) # Answer is 161289189

# Part 2: There are two new instructions you'll need to handle:

# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.

# example: xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# This time, the sum of the results is 48 (2*4 + 8*5)

# regex: mul\((\d+),(\d+)\)
# regex 2: |do\(\)|don't\(\)

# Regex patterns
mul_pattern = r'mul\((\d+),(\d+)\)'
control_pattern = r'do\(\)|don\'t\(\)'

# Combine patterns to match any instruction
combined_pattern = f'{mul_pattern}|{control_pattern}'

# Variables to track state
is_mul_enabled = True # cuz I know that the input starts without dont()
total2 = 0

# Iterate through matches
for match in re.finditer(combined_pattern, content):
    if match.group(0) == 'do()':
        is_mul_enabled = True
    elif match.group(0) == "don't()":
        is_mul_enabled = False
    elif is_mul_enabled and match.group(1) and match.group(2):  # Handle mul(x, y)
        x, y = int(match.group(1)), int(match.group(2))
        total2 += x * y

print("Total is:", total2) # Answer is: 83595109


